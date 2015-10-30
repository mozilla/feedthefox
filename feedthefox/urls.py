from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.flatpages import views


handler404 = 'feedthefox.base.views.custom_404'
handler500 = 'feedthefox.base.views.custom_500'

urlpatterns = patterns(
    '',
    url(r'^$', 'feedthefox.base.views.home', name='home'),
    url(r'^profile/$', 'feedthefox.base.views.profile', name='profile'),
    url(r'^porting/$', 'feedthefox.base.views.porting', name='porting'),
    url(r'^devices/$', 'feedthefox.devices.views.devices', name='devices'),
    url(r'^device/$', 'feedthefox.devices.views.device', name='device'),
    url(r'^dashboard/$', 'feedthefox.dashboard.views.dashboard', name='dashboard'),
    url(r'^gaia/$', views.flatpage, {'url': '/gaia/'}, name='gaia'),
    url(r'^b2gdroid/$', views.flatpage, {'url': '/b2gdroid/'}, name='b2gdroid'),
    url(r'^addons/$', views.flatpage, {'url': '/addons/'}, name='addons'),
    url('', include('feedthefox.users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^404/$', handler404),
        url(r'^500/$', handler500),
    )
