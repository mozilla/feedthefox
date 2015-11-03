from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from feedthefox.users.providers.github.provider import FeedTheFoxGitHubProvider


urlpatterns = default_urlpatterns(FeedTheFoxGitHubProvider)
