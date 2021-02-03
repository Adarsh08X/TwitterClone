"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from home.views import home, signup
from feed.views import feed, search
from notification.views import notifications
from feed.api import api_add_tweet, api_add_like
from Profile.views import twitterprofile, follow_tweeter, edit_profile,unfollow_tweeter


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('home.urls')),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),

    #feed app
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/', twitterprofile, name='twitterprofile'),
    path('u/<str:username>/follow/', follow_tweeter, name='follow_tweeter'),
    path('u/<str:username>/unfollow/', unfollow_tweeter, name='unfollow_tweeter'),

    #API
    path('api/add_tweet/', api_add_tweet, name='api_add_tweet'),
    path('api/add_like/', api_add_like, name='api_add_like'),

    path('notifications/', notifications, name='notifications'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
