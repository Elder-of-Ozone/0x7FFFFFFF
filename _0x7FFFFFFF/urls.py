"""_0x7FFFFFFF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^fitbit/$',fitbit),
    url(r'^blog/$', blog),
    url(r'^blog/technology/$', technology),
    url(ur'^blog/technology/(?P<entry>[^/]+)$', technology_blog_entry),
    url(r'^blog/environment/$', environment),
    url(r'^blog/environment/(?P<entry>[-\w]+)$', environment_blog_entry),
    url(ur'^blog/fitbit/(?P<entry>[^/]+)', fitbit_blog_entry),
    url(r'^blog/fitbit/$', fitbit_blog),
    url(r'^blog/life$', life),
)
