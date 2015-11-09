import importlib

from django.conf.urls import include, url

from allauth.account import views as account_views
from allauth.socialaccount import providers, views as socialaccount_views

from feedthefox.users import views


account_patterns = [
    url(r'^inactive/?$', account_views.account_inactive, name='account_inactive'),
    url(r'^signin/cancelled/?$', socialaccount_views.login_cancelled,
        name='socialaccount_login_cancelled'),
]


users_patterns = [
    url(r'^signin/?$', account_views.login, name='account_login'),
    url(r'^signout/?$', account_views.logout, name='account_logout'),
    url(r'^account/', include(account_patterns)),
]


# append to user_patterns, the provider's urls
for provider in providers.registry.get_list():
    try:
        provider_module = importlib.import_module(provider.package + '.urls')
    except ImportError:
        continue
    provider_urlpatterns = getattr(provider_module, 'urlpatterns', None)
    if provider_urlpatterns:
        users_patterns += provider_urlpatterns


urlpatterns = [
    url(r'^users/', include(users_patterns)),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^imei/(?P<imei>\d+)$', views.imei, name='imei'),
    url(r'^device-info/(?P<id>\d+)/delete$', views.delete_device_info,
        name='delete_device_info')
]
