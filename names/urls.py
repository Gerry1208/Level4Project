from django.conf.urls import patterns, url
from names import views

urlpatterns = patterns('',
                        url(r'^register/$', views.register, name='register'),
                        url(r'^index/$', views.index, name='index' ),
                        url(r'^login/$', views.user_login, name='login'),
                        url(r'^logout/$', views.user_logout, name='logout'),
                        url(r'^create/$', views.create_cards, name='create'),
                        url(r'^groups/$', views.groups, name='groups'),
                        url(r'^groupview/$', views.groupview, name='groupview'),
                       )
