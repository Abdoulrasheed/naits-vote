#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    
    url(r'^students/$', views.students, name='all_students_page'),
    #url(r'^executives/$', views.excos, name='all_excos_page'),
    url(r'^settings/password/$', views.change_password, name='change_password'),
    url(r'^profile/(.*)$', views.profile, name='profile'),
    url(r'^settings/edit/$', views.ProfileUpdate, name='edit_profile'),
    url(r'^notifications/$', views.check_messages, name="last_notifications"),
    url(r'^settings/picture/$', views.picture, name='picture'),
    url(r'^settings/upload_picture/$', views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', views.save_uploaded_picture,
        name='save_uploaded_picture'),
]