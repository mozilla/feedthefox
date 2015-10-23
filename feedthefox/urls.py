from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'feedthefox.base.views.home', name='home'),
    url(r'^devices/$', 'feedthefox.base.views.devices', name='devices'),
    url(r'^device/$', 'feedthefox.base.views.device', name='device'),
    url(r'^profile/$', 'feedthefox.base.views.profile', name='profile'),
    url(r'^porting/$', 'feedthefox.base.views.porting', name='porting'),
    url(r'^b2gdroid/$', 'feedthefox.base.views.b2gdroid', name='b2gdroid'),
    url(r'^dashboard/$', 'feedthefox.dashboard.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)
