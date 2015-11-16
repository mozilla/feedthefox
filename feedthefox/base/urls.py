from django.conf.urls import url

from feedthefox.base import views


urlpatterns = [
    url(r'^contribute.json$', views.contribute_view, name='contribute-view')
]
