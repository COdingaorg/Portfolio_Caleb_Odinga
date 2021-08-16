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