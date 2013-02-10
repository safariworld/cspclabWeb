from django.conf.urls.defaults import patterns, include, url
from home.views import *
from board.views import *
from plainPages.views import *
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

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':ROOT_PATH+'/media/'}),
    (r'^$', homeView),
    (r'^board/$', indexView),
    (r'^aboutus/$', aboutUsView),
)
