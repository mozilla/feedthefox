from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'feedthefox.base.views.home', name='home'),
    url(r'^profile/$', 'feedthefox.base.views.profile', name='profile'),
    url(r'^gaia/$', 'feedthefox.base.views.gaia', name='gaia'),
    url(r'^porting/$', 'feedthefox.base.views.porting', name='porting'),
    url(r'^b2gdroid/$', 'feedthefox.base.views.b2gdroid', name='b2gdroid'),
    url(r'^devices/$', 'feedthefox.devices.views.devices', name='devices'),
    url(r'^device/$', 'feedthefox.devices.views.device', name='device'),
    url(r'^dashboard/$', 'feedthefox.dashboard.views.dashboard', name='dashboard'),
    url('', include('feedthefox.users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
