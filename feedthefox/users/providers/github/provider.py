from allauth.account.models import EmailAddress
from allauth.socialaccount import providers
from allauth.socialaccount.providers.github.provider import GitHubProvider

from feedthefox.users.models import User


class FeedTheFoxGitHubProvider(GitHubProvider):
    """Custom GitHub provider that handles a list of emails
    from GitHub and adds them to the list of verified emails.
    """
    package = 'feedthefox.users.providers.github'

    def get_default_scope(self):
        """Use the "user:email" OAuth2 scope."""
        return ['user:email']

    def extract_email_addresses(self, data):
        """Extract only the verified emails from GitHub."""
        email_addresses = []
        for email_address in data.get('email_addresses', []):
            if email_address.get('verified', False):
                email_addresses.append(EmailAddress(email=email_address['email'],
                                                    verified=True,
                                                    primary=email_address['primary'],
                                                    user=User()))
        return email_addresses


providers.registry.register(FeedTheFoxGitHubProvider)
