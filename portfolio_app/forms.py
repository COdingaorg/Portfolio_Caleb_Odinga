from .models import Profile, Contact, Background, Skill, Tools, Social, Projects, Hobby
from django.contrib.auth import forms

class CreateProfile(forms.Form):
  class Meta:
    models = Profile
    exclude = ['user']

class ContactForm(forms.Form):
  class Meta:
    models = Contact
    exclude = ['profile']

class BackgroundForm(forms.Form):
  class Meta:
    models = Background
    exclude = ['profile']

class SkillForm(forms.Form):
  class Meta:
    models = Skill
    exclude = ['profile']

class ToolsForm(forms.Form):
  class Meta:
    models = Tools
    fields = ['__all__']

class SocialForm(forms.Form):
  class Meta:
    models = Social
    exclude = ['profile']

class ProjectsForm(forms.Form):
  class Meta:
    models = Projects
    exclude = ['profile']

class HobbyForm(forms.Form):
  class Meta:
    models = Hobby
    exclude = ['profile']