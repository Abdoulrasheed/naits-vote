"""naits_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views
from django.contrib import admin
from bitpoint.authentication.views import profile as profile_view

from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	url(r'^', include('bitpoint.voting.urls')),
    url(r'^settings/', include('bitpoint.authentication.urls')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('bitpoint.articles.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^messages/', include('bitpoint.messenger.urls')),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/accounts/login'}),
    url(r'^p/(.*)$', profile_view, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)