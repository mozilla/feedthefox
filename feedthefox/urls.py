from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views


handler404 = 'feedthefox.base.views.custom_404'
handler500 = 'feedthefox.base.views.custom_500'

urlpatterns = patterns(
    '',
    url(r'^$', 'feedthefox.base.views.home', name='home'),
    url(r'^devices/$', 'feedthefox.devices.views.devices', name='devices'),
    url(r'^device/(?P<manufacturer>[\w|\W]+)/(?P<model>[\w|\W]+)$', 'feedthefox.devices.views.device',
        name='device'),
    url(r'^device-info/(?P<id>\d+)/delete$', 'feedthefox.users.views.delete_device_info',
        name='delete_device_info'),
    url(r'^dashboard/$', 'feedthefox.dashboard.views.dashboard', name='dashboard'),
    url(r'^gaia/$', views.flatpage, {'url': '/gaia/'}, name='gaia'),
    url(r'^b2gdroid/$', views.flatpage, {'url': '/b2gdroid/'}, name='b2gdroid'),
    url(r'^addons/$', views.flatpage, {'url': '/addons/'}, name='addons'),
    url(r'^porting/$', views.flatpage, {'url': '/porting/'}, name='porting'),
    url(r'^fxos-tv/$', views.flatpage, {'url': '/fxos-tv/'}, name='fxos-tv'),
    url(r'^connect/$', views.flatpage, {'url': '/connect/'}, name='connect'),
    url(r'^foxfooding-about/$', views.flatpage, {'url': '/foxfooding-about/'},
        name='foxfooding_about'),
    url(r'^foxfooding-faq/$', views.flatpage, {'url': '/foxfooding-faq/'},
        name='foxfooding_faq'),
    url('', include('feedthefox.users.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^404/$', handler404),
        url(r'^500/$', handler500),
    )

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
