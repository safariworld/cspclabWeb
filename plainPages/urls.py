# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
import views

urlpatterns = patterns(
    'plainPages.views',
    (r'plain/account/signup/$', views.register),
    (r'plain/account/register_success/$', direct_to_template,
       { 'template' : 'registration/register_success.html' }),
    (r'aboutus$', views.aboutUs),
    (r'achievements$', views.achievements),
    (r'calendar$', views.calendar),
)

