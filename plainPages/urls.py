# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns(
    'plainPages.views',
    (r'^$', views.aboutUs),
)

