from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "pages/home.html")


@csrf_exempt
def create_superuser(request):
    if request.method == "POST":
        username1 = request.POST['username1']
        email1 = request.POST['email1']
        password1 = request.POST['password1']
        user = User.objects.create_user(username1, email1, password1)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        messages.success(request, "SuperUser Created Successfully")
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


@csrf_exempt
def create_adminuser(request):
    if request.method == "POST":
        username2 = request.POST['username2']
        email2 = request.POST['email2']
        password2 = request.POST['password2']
        user = User.objects.create_user(username2, email2, password2)
        user.is_staff = True
        user.save()
        messages.success(request, "AdminUser Created Successfully")
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")


@csrf_exempt
def create_normaluser(request):
    if request.method == "POST":
        username3 = request.POST['username3']
        email3 = request.POST['email3']
        password3 = request.POST['password3']
        User.objects.create_user(username3, email3, password3).save()
        messages.success(request, "NormalUser Created Successfully")
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
