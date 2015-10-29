from allauth.socialaccount.templatetags.socialaccount import get_providers

# return a list of social authentication providers
register.function(get_providers)
