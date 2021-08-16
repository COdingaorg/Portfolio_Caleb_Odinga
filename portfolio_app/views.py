from django.shortcuts import render

# Create your views here.

#view function to index page
def index(request):
  '''
  renders index page
  '''
  title = 'Home'
  context = {
    'title':title
  }

  return render(request, 'all_templates/index.html', context)

#view function to projects page
def projects(request):
  '''
  renders projects page
  '''
  title = 'Projects'
  context = {
    'title':title
  }
  return render(request, 'all_templates/projects.html', context)

#view function to projects page
def hobbies(request):
  '''
  renders hobbies page
  '''
  title = 'Fun side'
  context = {
    'title':title
  }
  return render(request, 'all_templates/hobbies.html', context)

#view function to projects page
def contacts(request):
  '''
  renders contacts page
  '''
  title = 'Contacts'
  context = {
    'title':title
  }
  return render(request, 'all_templates/index.html', context)
