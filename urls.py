# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
import os

ROOT_PATH = os.path.dirname(__file__)

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cspclabWeb.views.home', name='home'),
    # url(r'^cspclabWeb/', include('cspclabWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':ROOT_PATH+'/media/'}),
# modified by shpark
    url(r'^itemList/$', 'itemPage.views.itemListView'),
    url(r'^itemList/page/(?P<page>\d+)/$', 'itemPage.views.itemListView'),
    url(r'^', include('home.urls')),
    url(r'^board/', include('board.urls')),
    url(r'^plain/', include('plainPages.urls')),
    url(r'^accounts/signin/$', 'django.contrib.auth.views.login'),
)
