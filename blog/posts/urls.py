from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
