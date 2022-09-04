from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    
    course_name = models.CharField(max_length=200, unique=True, null=False)
    users = models.ManyToManyField(User, blank=True)
    description = models.TextField(max_length=200)
    cover_photo = models.ImageField(upload_to='cover_images', blank=True)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    photos = models.ImageField(upload_to='profile_photos', blank=True)
    courses = models.ManyToManyField(Course, blank=True,null=True)

class CourseVideos(models.Model):
    course_a = models.ForeignKey(Course, on_delete=models.CASCADE)
    videos = models.FileField(upload_to='videos', blank=True)