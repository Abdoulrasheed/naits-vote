from django.urls import path

from bitpoint.articles import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('write/', views.CreateArticle.as_view(), name='write'),
    path('preview/', views.preview, name='preview'),
    path('drafts/', views.drafts, name='drafts'),
    path('comment/', views.comment, name='comment'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('edit/<int:pk>/', 
    	views.EditArticle.as_view(), name='edit_article'),
    path('<slug:slug>', views.article, name='article'),
]
