# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns(
    'board.views',
    url(r'^list/(?P<board_category>[^/]+)/(?P<page>[^/]+)/$', views.list),
    url(r'^read/(?P<entry_id>[0-9]+)/$', views.read),
    url(r'^write/(?P<board_category>[^/]+)/$', views.write),
    url(r'^download/attachments/(?P<filename>.*)/$', views.download_file),
)
