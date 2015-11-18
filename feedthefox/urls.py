from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'feedthefox.base.views.custom_404'
handler500 = 'feedthefox.base.views.custom_500'

urlpatterns = [
    # Base urls
    url('', include('feedthefox.base.urls')),
    # Users urls
    url('', include('feedthefox.users.urls')),
    # Devices urls
    url('', include('feedthefox.devices.urls')),
    # Dashboard urls
    url('', include('feedthefox.dashboard.urls')),
    # Admin urls
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^404/$', handler404),
        url(r'^500/$', handler500),
    )

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
