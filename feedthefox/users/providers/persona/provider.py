from allauth.socialaccount import providers
from allauth.socialaccount.providers.provider import PersonaProvider


class FeedTheFoxPersonaProvider(PersonaProvider):
    package = 'feedthefox.users.providers.persona'


providers.registry.register(FeedTheFoxPersonaProvider)
