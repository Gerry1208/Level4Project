from django.conf.urls import patterns, url
from names import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
                        url(r'^register/$', views.register, name='register'),
                        url(r'^index/$', views.index, name='index'),
                        url(r'^login/$', views.user_login, name='login'),
                        url(r'^logout/$', views.user_logout, name='logout'),
                        url(r'^create/$', views.create_cards, name='create'),
                        url(r'^groups/$', views.groupview, name='groupview'),
                        url(r'^cardview/$', views.cardview, name='cardview'),
                        url(r'^readyquiz/$', views.quiz, name='readyquiz'),
                        url(r'^upload/$', views.upload, name='upload'),
                        url(r'^addpicture/$', views.addPicture, name='addpicture'),
                        url(r'^selfmark/$', views.SelfMarkQuiz, name='selfmark'),
                        url(r'^quiz/$', views.nextQuestion, name='quiz'),
                        url(r'^complete/$', views.complete, name='complete')
                       )
