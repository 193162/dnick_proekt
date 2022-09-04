from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from courses.forms import MyUserLogin, MyUserRegister, ProfileForm
from courses.models import Course, Profile, CourseVideos
from math import floor, ceil


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'home.html', context=context)
    else:
        context = {'user': None}
        return render(request, 'home.html', context=context)


def pricing(request):
    context = {}

    return render(request, 'pricing.html', context=context)


def contact(request):
    context = {}

    return render(request, 'contact.html', context=context)


def courses(request, pckg):
    formRegister = MyUserRegister(request.POST)
    formLogin = MyUserLogin(request.POST)

    print(request.POST)
    print(request.POST.get('Register'))
    if pckg == "BASIC":
        tmp = User.objects.get(id=request.user.id)
        tmp.type_of_package = pckg
        tmp.save()
    elif pckg == "STANDARD":
        tmp = User.objects.get(id=request.user.id)
        tmp.type_of_package = pckg
        tmp.save()
    elif pckg == "STANDARD_PLUS":
        tmp = User.objects.get(id=request.user.id)
        tmp.type_of_package = pckg
        tmp.save()
    else:
        tmp = User.objects.get(id=request.user.id)
        tmp.type_of_package = "BASIC"
        tmp.save()

    formRegister = MyUserRegister(request.POST)
    formLogin = MyUserLogin(request.POST)

    print(request.POST)
    print(request.POST.get('Register'))
    if request.POST.get('Register') is not None:
        print(formRegister.errors)
        if formRegister.is_valid():
            registered_user = formRegister.save()
            login(request, registered_user)

        Profile.objects.create(username=request.user)
        # print(formProfile)

    if request.POST.get('Login') is not None:
        if authenticate(username=formLogin.data['username'], password=formLogin.data['password']) is not None:
            user = authenticate(username=formLogin.data['username'], password=formLogin.data['password'])
            login(request, user)

    courses = Course.objects.all()
    num_courses = Course.objects.all().count()

    context = {'courses': courses, 'user': request.user, 'package': pckg}
    return render(request, 'courses.html', context=context)




def profile(request, id):
    print("Wallace")
    print(request.POST)

    if bool(request.POST):
        course = Course.objects.get(id=id)
        course.users.add(request.user)
        profile_1 = Profile.objects.get(username=request.user.id)
        profile_1.courses.add(course)

        print(request.user.id)
        profile = Profile.objects.get(username=request.user.id)

        context = {"profile": profile}
        return render(request, 'profile.html', context=context)
    else:
        print("Redirect")

        print(request.user.id)
        course = Course.objects.get(id=id)
        course.users.add(request.user)
        profile_1 = Profile.objects.get(username=request.user.id)
        profile_1.courses.add(course)
        profile = Profile.objects.get(username=request.user.id)

        context = {"profile": profile}
        return render(request, 'profile.html', context=context)


def course_view(request, id, pckg):
    if pckg == 'none':
        course_help = Course.objects.get(id=id)
        course = Course.objects.filter(id=id)
        print(course_help.id)
        course_videos = CourseVideos.objects.filter(course_a=course_help.id)
        context = {"course": course, "user": request.user, 'course_videos': course_videos, 'package': pckg}
        return render(request, 'course_view.html', context=context)
    else:
        course_help = Course.objects.get(id=id)
        course = Course.objects.filter(id=id)
        print(course_help.id)
        course_videos = CourseVideos.objects.filter(course_a=course_help.id)
        context = {"course": course, "user": request.user, 'course_videos': course_videos}
        return render(request, 'course_view.html', context=context)


def my_login(request):
    form = MyUserLogin()
    context = {'form': form}
    return render(request, 'login.html', context=context)


def my_register(request):
    form = MyUserRegister()

    context = {'form': form}
    return render(request, 'register.html', context=context)
