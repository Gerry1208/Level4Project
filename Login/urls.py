from django.conf.urls import patterns, url
from Login import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='Login'))