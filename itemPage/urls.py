# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('itemPage.views',
        url(r'^$', views.itemListView),
        url(r'^page/(?P<page>\d+)/$', views.itemListView),
)
