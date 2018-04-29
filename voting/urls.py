#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile, name='profile'),
    url(r'^students/$', views.students, name='all_students_page'),
]