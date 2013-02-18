# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns(
    'plainPages.views',
    (r'aboutus$', views.aboutUs),
    (r'achievements$', views.achievements),
)

