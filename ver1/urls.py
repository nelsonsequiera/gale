'''
Created on 03-Dec-2015

@author: nell
'''
from django.conf.urls import patterns, url
from ver1 import views

urlpatterns = patterns('',
                       url(r'^index$', views.index, name = 'index'),
                       url(r'^page/(?P<id_num>[\0-9]+)/$', views.page, name = 'page'),
                       url(r'^base$', views.base, name = 'base')
                       )