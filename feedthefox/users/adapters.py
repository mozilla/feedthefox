from django.conf import settings

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import setup_user_email
from allauth.socialaccount.helpers import _login_social_account
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import EmailAddress

from feedthefox.users.models import User
from feedthefox.users.mozillians import MozilliansClient


class FeedTheFoxAdapter(DefaultAccountAdapter):
    """Customize the default allauth account adapter."""

    def is_open_for_signup(self, request):
        """Disable signup since everything will go through Persona."""

        return False


class FeedTheFoxSocialAdapter(DefaultSocialAccountAdapter):

    def __init__(self, *args, **kwargs):
        """Initialize mozillians.org api client."""

        super(FeedTheFoxSocialAdapter, self).__init__(*args, **kwargs)
        self.mozillians_client = MozilliansClient(settings.MOZILLIANS_API_URL,
                                                  settings.MOZILLIANS_API_KEY)

    def is_open_for_signup(self, request, sociallogin):
        """ Enable signup only through social accounts."""

        return True

    def populate_user(self, request, sociallogin, data):
        """Populate user with data from mozillians.org."""

        mozillian_attrs = ['country', 'photo', 'ircname', 'city']
        user = super(FeedTheFoxSocialAdapter, self).populate_user(request,
                                                                  sociallogin,
                                                                  data)
        emails = []

        if sociallogin.account.provider == 'github':
            for email_address in sociallogin.email_addresses:
                email_address.user = sociallogin.user
                if email_address.primary:
                    sociallogin.user.email = email_address.email
                emails.append(email_address.email)
        else:
            emails.append(user.email)

        for email in emails:
            try:
                mozillian = self.mozillians_client.lookup_user({'email': email})
                break
            except:
                mozillian = None

        if mozillian:
            user.username = mozillian['username']
            user.mozillian_username = mozillian['username']
            for attr in mozillian_attrs:
                if mozillian[attr].get('privacy') == 'Public':
                    setattr(user, attr, mozillian[attr].get('value'))
            if mozillian['full_name']['privacy'] == 'Public':
                first_name, last_name = mozillian['full_name']['value'].split(' ', 1)
            else:
                first_name = 'Anonymous'
                last_name = 'Mozillian'
            user.first_name = first_name
            user.last_name = last_name
        else:
            user.is_active = False
        return user

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
            sociallogin.user = user
            if sociallogin.is_existing:
                # Social Account already connected, signin please
                _login_social_account(request, sociallogin)
            else:
                sociallogin.account.user = user
                sociallogin.account.save()
                if sociallogin.token:
                    sociallogin.token.account = sociallogin.account
                    sociallogin.token.save()
                if not EmailAddress.objects.filter(user=user).exists():
                    setup_user_email(request, user, sociallogin.email_addresses)
