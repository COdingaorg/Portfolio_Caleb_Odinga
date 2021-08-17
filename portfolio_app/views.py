from django.contrib import messages
from portfolio_app.forms import BackgroundForm, ContactForm, CreateProfile, HobbyForm, ProjectsForm, SkillForm, SocialForm, ToolsForm
from django.shortcuts import redirect, render
from .models import Profile, Projects, Skill, Tools, User

# Create your views here.

#-----------------------------------------------------------------------------------------------------
#global variables
user = User.objects.filter(username__icontains = 'caleb', last_name__icontains = 'odinga', email = 'calemasanga@gmail.com' ).last()
main_profile = Profile.objects.filter(user = user).last()

#view function to index page
def index(request):
  '''
  renders index page
  '''
  title = 'Home'
  context = {
    'user': user,
    'profile':main_profile,
    'title':title
  }

  return render(request, 'all_templates/index.html', context)

#view function to projects page
def projects(request):
  '''
  renders projects page
  '''
  skills = Skill.objects.filter(profile = main_profile)
  title = 'Projects'
  projects = Projects.objects.filter(profile = main_profile)
  context = {
    'projects':projects,
    'skills':skills,    
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
    'user': user,
    'profile':main_profile,
    'title':title
  }
  return render(request, 'all_templates/hobbies.html', context)

#view function to projects page
def contacts(request):
  '''
  renders contacts page
  '''

  if request.method == "POST" and 'update_profile' in request.POST:
    form = ContactForm(request.POST)
    if form.is_valid():
      new_contact = form.save(commit = False)
      new_contact.profile = main_profile
      new_contact.save()

      messages.success(request, 'Contact created successfully')
      return redirect('profile')
  else: 
    form = ContactForm
    title = 'Contacts'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/contact.html', context)

#view function to profile page
def profile(request):
  '''
  renders profile page
  '''
  if request.method == "POST" and 'update_profile' in request.POST:
    form = CreateProfile(request.POST, request.FILES)
    if form.is_valid():
      new_profile = form.save(commit = False)
      new_profile.user = user
      new_profile.save()

      messages.success(request, 'Profile created successfully')
      return redirect('profile')
  else: 
    form = CreateProfile
    title = 'Admin Profile  '
    context = {
      'user':user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/profile.html', context)

#view function to background page
def background(request):
  '''
  renders background page
  '''
  if request.method == "POST" and 'update_profile' in request.POST:
    form = BackgroundForm(request.POST)
    if form.is_valid():
      new_profile = form.save(commit = False)
      new_profile.user = user
      new_profile.save()

      messages.success(request, 'Background created successfully')
      return redirect('profile')
  else: 
    form = BackgroundForm
    title = 'background'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title,
    }
    return render(request, 'all_templates/background.html', context)

#view function to skill page
def skills(request):
  '''
  renders skills page
  '''

  if request.method == "POST" and 'skills' in request.POST:
    form = SkillForm(request.POST, request.FILES)
    if form.is_valid():
      new_skill = form.save(commit = False)
      new_skill.profile = main_profile
      new_skill.save()

      messages.success(request, 'Skill Added successfully')
      return redirect('skills')
    else:
      messages.warning(request, 'Invalid Form')
  else: 
    form = SkillForm
    title = 'skills'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/skills.html', context)

#view function to tools page
def tools(request):
  '''
  renders tools page
  '''

  if request.method == "POST" and 'update_profile' in request.POST:
    form = ToolsForm(request.POST, request.FILES)
    if form.is_valid():
      new_tool = form.save(commit = False)
      new_tool.save()

      messages.success(request, 'Tool added successfully')
      return redirect('tools')
    else:
      messages.warning(request, 'Invalid Form or Input')
      return redirect('tools')
  else: 
    form = ToolsForm
    title = 'tools'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/tools.html', context)

#view function to social page
def social(request):
  '''
  renders social accounts page
  '''

  if request.method == "POST" and 'update_profile' in request.POST:
    form = SocialForm(request.POST, request.FILES)
    if form.is_valid():
      new_social = form.save(commit = False)
      new_social.profile = main_profile
      new_social.save()

      messages.success(request, 'new Social created successfully')
      return redirect('social')
  else: 
    form = SocialForm
    title = 'social'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/social.html', context)

#view function to hobby form page
def hobbyform(request):
  '''
  renders hobby form page
  '''

  if request.method == "POST" and 'update_profile' in request.POST:
    form = HobbyForm(request.POST, request.FILES)
    if form.is_valid():
      new_profile = form.save(commit = False)
      new_profile.user = user
      new_profile.save()

      messages.success(request, 'Profile created successfully')
      return redirect('profile')
  else: 
    form = HobbyForm
    title = 'hobby'
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/social.html', context)

#view function to project form page
def projectform(request):
  '''
  renders project form page
  '''

  if request.method == "POST" and 'update_profile' in request.POST:
    form = ProjectsForm(request.POST, request.FILES)
    if form.is_valid():
      new_project = form.save(commit = False)
      new_project.profile = main_profile
      new_project.save()

      messages.success(request, 'Project created successfully')
      return redirect('projectform')
  else: 
    
    form = ProjectsForm
    title = 'project'
    
    context = {
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/project_form.html', context)

