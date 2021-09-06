"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
import rest_framework
from portfolio_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'background', views.BackgroundViewSet)
router.register(r'contact', views.ContactViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'tools', views.ToolsViewSet)
router.register(r'social', views.SocialViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'hobby', views.HobbyViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace = 'rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tinymce/', include('tinymce.urls'))
]
