from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
