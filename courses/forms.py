from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.contrib.auth.models import User
from courses.models import Course, Profile

class MyUserLogin(forms.ModelForm):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()   
        return username
    def clean_password(self):  
        pass_word = self.cleaned_data['password']    
        return pass_word  
    class Meta:
        model = User
        fields = ['username','password']

class MyUserRegister(UserCreationForm):

    username = forms.CharField(label='username', max_length=150)  
    email = forms.EmailField(label='email')
    is_teacher = forms.BooleanField(label='Are you a teacher', required=False)
    type_of_package = forms.CharField(max_length=100, required=False)  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'], 
            self.cleaned_data['is_teacher'], 
            self.cleaned_data['type_of_package'],
        )  
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['photos'].required = False
        self.fields['courses'].required = False

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['users'].required = False
        self.fields['cover_photo'].required = False
        self.fields['videos'].required = False