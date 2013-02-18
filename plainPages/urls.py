# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
import views

urlpatterns = patterns(
    'plainPages.views',
    (r'^$', views.aboutUs),
    (r'^/account/signup/$', views.register),
    (r'^/account/register_success/$', direct_to_template,
       { 'template' : 'registration/register_success.html' }),
)

