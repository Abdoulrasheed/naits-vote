from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('<int:pk>)/', login_required(views.DetailView.as_view()), name='detail'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    
    path('students/', views.students, name='students'),
    path('staffs/', views.staffs, name='staffs'),
    path('excos/', views.excos, name='excos'),
]