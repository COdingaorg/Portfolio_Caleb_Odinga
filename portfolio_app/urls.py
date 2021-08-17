from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^projects/$', views.projects, name = 'project'),
  url(r'^hobbies/$', views.hobbies, name = 'hobby'),
  url(r'^contact/$', views.contacts, name = 'contact'),
  url(r'^profile/$', views.profile, name = 'profile'),
  url(r'^background/$', views.background, name = 'background'),
  url(r'^skills/$', views.skills, name = 'skills'),
  url(r'^tools/$', views.tools, name = 'tools'),
  url(r'^social/$', views.social, name = 'social'),
  url(r'^hobby/$', views.hobbyform, name = 'hobbyform'),
  url(r'^projectform/$', views.projectform, name = 'projectform'),
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)