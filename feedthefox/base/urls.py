from django.conf.urls import url
from django.contrib.flatpages import views as flatpages_views

from feedthefox.base import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contribute.json$', views.contribute_view, name='contribute-view'),
    # Contribute flatpages
    url(r'^gaia/$', flatpages_views.flatpage, {'url': '/gaia/'}, name='gaia'),
    url(r'^b2gdroid/$', flatpages_views.flatpage, {'url': '/b2gdroid/'}, name='b2gdroid'),
    url(r'^addons/$', flatpages_views.flatpage, {'url': '/addons/'}, name='addons'),
    url(r'^porting/$', flatpages_views.flatpage, {'url': '/porting/'}, name='porting'),
    url(r'^fxos-tv/$', flatpages_views.flatpage, {'url': '/fxos-tv/'}, name='fxos-tv'),
    url(r'^connect/$', flatpages_views.flatpage, {'url': '/connect/'}, name='connect'),
    # Flatpages urls
    url(r'^foxfooding-about/$', flatpages_views.flatpage, {'url': '/foxfooding-about/'},
        name='foxfooding_about'),
    url(r'^foxfooding-faq/$', flatpages_views.flatpage, {'url': '/foxfooding-faq/'},
        name='foxfooding_faq')
]
