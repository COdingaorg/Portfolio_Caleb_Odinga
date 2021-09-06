from rest_framework import serializers
from .models import Profile, Contact, Background, Skill, Tools, Social, Projects, Hobby, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email', 'is_active']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True, required = False)
    serializers.ImageField(use_url = True)
    
    class Meta:
        model = Profile
        fields = ['user', 'photo_path', 'intro_message', 'tagline', 'mantra']

class ContactSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Contact
        fields = ['contact_title', 'contact', 'profile']

class BackgroundSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Background
        fields = ['title', 'description', 'links', 'profile']

class SkillSerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url = True)
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Skill
        fields = ['title', 'description', 'images_path', 'profile']

class ToolsSerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url = True)
    skill = SkillSerializer(read_only = True)
    class Meta:
        model = Tools
        fields = ['title', 'description', 'image_path', 'skill']

class SocialSerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url = True)
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Social
        fields = ['platform', 'photo_path', 'username', 'profile']

class ProjectsSerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url = True)
    skill = SkillSerializer(many = True, read_only = True)
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Projects
        fields = ['title', 'description', 'image_path', 'skill', 'profile']

class HobbySerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url = True)
    serializers.FileField(use_url = True)
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = Hobby
        fields = ['title', 'description', 'image_path', 'file_path', 'profile']