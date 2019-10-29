from django.urls import path

from bitpoint.messenger import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('send/', views.send, name='send_message'),
    path('check/', views.check, name='check_message'),
    path('delete/', views.delete, name='delete_message'),
    path('receive/', views.receive, name='receive_message'),
    path('<str:ID_Number>/', views.messages, name='messages'),
]
