# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns(
    'board.views',
    url(r'^list/(?P<board_category>[^/]+)/(?P<page>[^/]+)/$', views.list, name="board-list"),
    url(r'^read/(?P<entry_id>[0-9]+)/$', views.read, name="board-read"),
    url(r'^edit/(?P<entry_id>[0-9]+)/$', views.write, name="board-edit"),
    url(r'^delete/(?P<entry_id>[0-9]+)/$', views.delete, name="board-delete"),
    url(r'^write/(?P<board_category>[^/]+)/$', views.write),
    url(r'^download/attachments/(?P<filename>.*)/$', views.download_file),
    url(r'^add_comment/', views.add_comment),
)
