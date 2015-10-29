from django.conf.urls import url

from allauth.socialaccount.providers.persona import views as persona_views


urlpatterns = [
    url(r'^persona/signin$', persona_views.persona_login, name='persona_login'),
]
