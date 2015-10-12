from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'feedthefox.base.views.home', name='home'),
    url(r'^devices/$', 'feedthefox.base.views.devices', name='devices'),
    url(r'^device/$', 'feedthefox.base.views.device', name='device'),
    url(r'^dashboard/$', 'feedthefox.dashboard.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
