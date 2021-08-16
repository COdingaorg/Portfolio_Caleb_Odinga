from django.db import models
from django.db.models.deletion import CASCADE
from tinymce import models as tiny_model
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=CASCADE)
  photo_path = models.ImageField(upload_to = 'Profile/')
  intro_message = tiny_model.HTMLField()
  tagline = models.TextField()
  mantra = models.CharField(max_length=256, blank=True, null=True)

  def __str__(self):
      return self.user.username

class Contact(models.Model):
  contact_title = models.CharField(max_length=100, unique=True)
  contact = models.CharField(max_length=50)
  profile = models.ForeignKey(Profile,on_delete=CASCADE)

  def __str__(self):
    return self.contact_title

class Background(models.Model):
  title = models.CharField(max_length = 200)
  description = tiny_model.HTMLField()
  links = models.CharField(max_length=256)
  profile = models.ForeignKey(Profile, on_delete=CASCADE)

  def __str__(self):
    return self.title

class Skill(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  images_path = models.ImageField(upload_to = 'Skills/')
  profile = models.ForeignKey(Profile, on_delete=CASCADE)

  def __str__(self):
    return self.title

class Tools(models.Model):
  title = models.CharField(max_length=256)
  description = models.TextField()
  image_path = models.ImageField(upload_to = 'Tools/')
  skill = models.ForeignKey(Skill, on_delete=CASCADE)

  def __str__(self):
    return self.title


class Social(models.Model):
  platform = models.CharField(max_length=100)
  photo_path = models.ImageField(upload_to = 'Social/')
  username = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile, on_delete=CASCADE)

  def __str__(self):
    return self.platform

class Projects(models.Model):
  title = models.CharField(max_length=256)
  description = tiny_model.HTMLField()
  image_path = models.ImageField(upload_to = 'Projects/')
  skill = models.ForeignKey(Skill, on_delete=CASCADE)
  profile = models.ForeignKey(Profile, on_delete=CASCADE)

  def __str__(self):
    return self.title

class Hobby(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  image_path = models.ImageField(upload_to = 'Hobbies/')
  file_path = models.FileField(upload_to='Hobbies/')
  profile = models.ForeignKey(Profile, on_delete=CASCADE)

  def __str__(self):
    return self.title