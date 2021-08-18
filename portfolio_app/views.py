from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from portfolio_app.forms import BackgroundForm, ContactForm, CreateProfile, HobbyForm, ProjectsForm, SkillForm, SocialForm, ToolsForm, LoginForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Background, Contact, Profile, Projects, Skill, Tools, User

# Create your views here.

#-----------------------------------------------------------------------------------------------------
#global variables
user = User.objects.filter(username__icontains = 'caleb', last_name__icontains = 'odinga', email = 'calemasanga@gmail.com' ).last()
main_profile = Profile.objects.filter(user = user).last()
contacts = Contact.objects.filter(profile = main_profile)

#login user
def login_user(request):
  title = 'Login to Your Account'
  form = LoginForm
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    newlogin =  authenticate(request, username = username, password = password)
    if newlogin:
      login(request, newlogin)

      messages.success(request, 'Login successful. Add Profile to proceed')
      return redirect('/')

    else:
      messages.warning(request, 'Incorrect Username or Password')
      return redirect('login_user')
  
  
  context = {
    'title':title,
    'form':form,
    }

  return render(request, 'registration/login.html', context)

#view function to index page
def index(request):
  '''
  renders index page
  '''
  title = 'Home'
  tools = Tools.objects.all()
  background = Background.objects.all()
  context = {
    'background':background,
    'contacts':contacts,
    'tools':tools,
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
    'contacts':contacts,
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
    'contacts':contacts,
    'user': user,
    'profile':main_profile,
    'title':title
  }
  return render(request, 'all_templates/hobbies.html', context)

#view function to projects page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/contact.html', context)

#view function to profile page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user':user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/profile.html', context)

#view function to background page
@login_required(login_url='/')
def background(request):
  '''
  renders background page
  '''
  if request.method == "POST" and 'update_profile' in request.POST:
    form = BackgroundForm(request.POST)
    if form.is_valid():
      new_background = form.save(commit = False)
      new_background.profile = main_profile
      new_background.save()

      messages.success(request, 'Background created successfully')
      return redirect('profile')
  else: 
    form = BackgroundForm
    title = 'background'
    context = {
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title,
    }
    return render(request, 'all_templates/background.html', context)

#view function to skill page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/skills.html', context)

#view function to tools page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/tools.html', context)

#view function to social page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/social.html', context)

#view function to hobby form page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/social.html', context)

#view function to project form page
@login_required(login_url='/')
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
      'contacts':contacts,
      'user': user,
      'profile':main_profile,
      'form':form,
      'title':title
    }
    return render(request, 'all_templates/project_form.html', context)

