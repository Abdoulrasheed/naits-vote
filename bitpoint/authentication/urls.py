from django.urls import path
from .import views


urlpatterns = [
    path('', views.ProfileUpdate, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    path('picture/', views.picture, name='picture'),
    path('upload_picture/', views.upload_picture, name='upload_picture'),
    path('save_uploaded_picture/', views.save_uploaded_picture, name='save_uploaded_picture'),
]