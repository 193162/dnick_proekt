from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from courses.models import Course, Profile, CourseVideos

admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(CourseVideos)
# Register your models here.

