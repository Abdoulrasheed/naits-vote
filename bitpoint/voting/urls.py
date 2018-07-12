#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
    url(r'^students/$', views.students, name='students'),
    url(r'^staffs/$', views.staffs, name='staffs'),
    url(r'^excos/$', views.excos, name='excos'),
]