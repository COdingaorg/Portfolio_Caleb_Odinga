from .models import Profile, Contact, Background, Skill, Tools, Social, Projects, Hobby
from django import forms

class CreateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['photo_path', 'intro_message','tagline', 'mantra']

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    exclude = ['profile']

class BackgroundForm(forms.ModelForm):
  class Meta:
    model = Background
    exclude = ['profile']

class SkillForm(forms.ModelForm):
  class Meta:
    model = Skill
    exclude = ['profile']

class ToolsForm(forms.ModelForm):
  class Meta:
    model = Tools
    fields = ('__all__')

class SocialForm(forms.ModelForm):
  class Meta:
    model = Social
    exclude = ['profile']

class ProjectsForm(forms.ModelForm):
  class Meta:
    model = Projects
    exclude = ['profile']

class HobbyForm(forms.ModelForm):
  class Meta:
    model = Hobby
    exclude = ['profile']