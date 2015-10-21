from django.conf.urls import patterns, url
from Login import views

urlpatterns = patterns('',
                        url(r'^register/$', views.register, name='register'),
                        url(r'^login/$', views.user_login, name='login'),
                       )
