from django.urls import path

from bitpoint.messenger import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send, name='send_message'),
    path('new/', views.new, name='new_message'),
    path('check/', views.check, name='check_message'),
    path('users/', views.users, name='users_message'),
    path('delete/', views.delete, name='delete_message'),
    path('<str:user_id>/', views.messages, name='messages'),
]
