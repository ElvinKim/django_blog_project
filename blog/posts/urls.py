from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<id>\d+)/update/$', post_update, name="update"),
    url(r'^delete/$', post_delete),
]
