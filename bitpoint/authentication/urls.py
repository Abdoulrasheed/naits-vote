#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProfileUpdate, name='edit_profile'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^picture/$', views.picture, name='picture'),
    url(r'^upload_picture/$', views.upload_picture, name='upload_picture'),
    url(r'^save_uploaded_picture/$', views.save_uploaded_picture, name='save_uploaded_picture'),
]