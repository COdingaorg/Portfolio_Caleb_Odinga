from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^projects/$', views.projects, name = 'project'),
  url(r'^hobbies/$', views.hobbies, name = 'hobby'),
  url(r'^contact/$', views.contacts, name = 'contact')
]