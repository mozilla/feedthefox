from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import cleanup_email_addresses
from allauth.socialaccount.helpers import _login_social_account
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import EmailAddress

from feedthefox.users.models import User
from feedthefox.users.mozillians import MozilliansClient


def populate_user_data(user, sociallogin, mozillian_profile=None):
    """Populates user instance with data gathered from mozillians.org."""
    mozillian_attrs = ['country', 'photo', 'ircname', 'city']

    if mozillian_profile:
        user.mozillian_username = mozillian_profile['username']
        for attr in mozillian_attrs:
            if mozillian_profile[attr].get('privacy') == 'Public':
                setattr(user, attr, mozillian_profile[attr].get('value'))
        if mozillian_profile['full_name']['privacy'] == 'Public':
            full_name = mozillian_profile['full_name']['value'].split(' ', 1)
            try:
                first_name, last_name = full_name
            except ValueError:
                first_name = full_name[0]
                last_name = ''
        else:
            first_name = 'Anonymous'
            last_name = 'Mozillian'
        user.first_name = first_name
        user.last_name = last_name

        # Add all the emails from both the providers and mozillians.org
        if not sociallogin.is_existing:
            mozillian_emails = []
            for email_addr in mozillian_profile['alternate_emails']:
                mozillian_emails.append(email_addr['email'])
            social_email_addresses = [addr.email for addr in sociallogin.email_addresses]
            all_emails = list(set(social_email_addresses) | set(mozillian_emails))
            for email in all_emails:
                sociallogin.email_addresses.append(EmailAddress(user=user,
                                                                email=email,
                                                                verified=True,
                                                                primary=False))

            primary_email = mozillian_profile['email'].get('value')
            sociallogin.email_addresses.append(EmailAddress(user=user,
                                                            email=primary_email,
                                                            verified=True,
                                                            primary=True))
    else:
        user.is_active = False

    return user


def get_mozillian_profile(emails):
    """Return a profile from mozillians.org give a list of emails."""

    # Check that settings for mozillians.org API are present
    if not settings.MOZILLIANS_API_URL or not settings.MOZILLIANS_API_KEY:
        raise ImproperlyConfigured('No API_KEY or URL configured. '
                                   'Please provide MOZILLIANS_API_URL and '
                                   'MOZILLIANS_API_KEY in the settings.')
    mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                         settings.MOZILLIANS_API_KEY)

    profile = None
    for email in emails:
        try:
            profile = mozillians_client.lookup_user({'email': email})
            break
        except:
            pass
    return profile


class FeedTheFoxAdapter(DefaultAccountAdapter):
    """Customize the default allauth account adapter."""

    def is_open_for_signup(self, request):
        """Disable signup since everything will go through Persona."""

        return False


class FeedTheFoxSocialAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        """ Enable signup only through social accounts."""

        return True

    def populate_user(self, request, sociallogin, data):
        """Populate user with data from mozillians.org."""

        user = super(FeedTheFoxSocialAdapter, self).populate_user(request, sociallogin, data)
        emails = []

        for email_address in sociallogin.email_addresses:
            email_address.user = sociallogin.user

            if email_address.primary:
                sociallogin.user.email = email_address.email
            emails.append(email_address.email)

        mozillian = get_mozillian_profile(emails)
        return populate_user_data(user, sociallogin, mozillian)

    def pre_social_login(self, request, sociallogin):
        email = sociallogin.user.email

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        emails_query = EmailAddress.objects.filter(email=email)
        if not user and emails_query.exists():
            user = emails_query[0].user

        if user:
            # If this is a new social account, connect it please
            sociallogin.user = user

            # Add additional emails, if any
            addresses, primary = cleanup_email_addresses(request, sociallogin.email_addresses)

            for address in addresses:
                address.user = user
                address.save()

            # If the cleanup_email_addresses does not return something, get the mozillians.org
            # primary email
            if not primary:
                primary_emails = [addr for addr in sociallogin.email_addresses
                                  if addr.primary]
                if primary_emails:
                    # The last email is the primary from mozillians.org
                    primary = primary_emails[-1]

            user.email = primary.email
            user.save()
            EmailAddress.objects.filter(user=user).update(primary=False)
            EmailAddress.objects.filter(user=user, email=primary.email).update(primary=True)

            if sociallogin.is_existing:
                # Social Account already connected, signin please
                _login_social_account(request, sociallogin)
            else:
                # Let's connect the account first
                sociallogin.connect(request, user)
