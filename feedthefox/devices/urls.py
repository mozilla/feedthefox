from django.conf.urls import url

from feedthefox.devices import views


urlpatterns = [
    url(r'^devices/$', views.devices, name='devices'),
    url(r'^device/(?P<manufacturer>[\w|\W]+)/(?P<model>[\w|\W]+)$',
        views.device, name='device')
]
