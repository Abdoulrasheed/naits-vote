from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin
from bitpoint.authentication.views import profile as profile_view
from bitpoint.activities import views as activities_views

from .import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', include('bitpoint.voting.urls')),
    path('settings/', include('bitpoint.authentication.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('articles/', include('bitpoint.articles.urls')),

    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LoginView.as_view(template_name='registration/login.html'), name='logout', kwargs={'next_page': '/accounts/login'}),
    path('messages/', include('bitpoint.messenger.urls')),
    path('user/<int:student_id>/', profile_view, name='profile'),
    path('notifications/', activities_views.notifications, name='notifications'),
    path('notifications/last/', activities_views.last_notifications, name='last_notifications'),
    path('notifications/check/', activities_views.check_notifications,
        name='check_notifications'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)