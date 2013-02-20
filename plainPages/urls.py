# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login
import views

urlpatterns = patterns(
    'plainPages.views',
    (r'accounts/signin/$', login),
    (r'accounts/signup/$', views.register),
    (r'accounts/register_success/$', direct_to_template,
       { 'template' : 'registration/signup_success.html' }),
    (r'aboutus$', views.aboutUs),
    (r'achievements$', views.achievements),
    (r'calendar$', views.calendar),
    (r'logout$', views.logout_page),
    (r'profile$', views.profile),
)

