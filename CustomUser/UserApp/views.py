from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request,"pages/home.html")

def create_superuser(request):
    if request.method == "POST":
        username1 = request.POST['username1']
        email1 = request.POST['email1']
        password1 = request.POST['password1']
        print(username1,email1,password1)
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def create_adminuser(request):
    if request.method == "POST":
        username2 = request.POST['username2']
        email2 = request.POST['email2']
        password2 = request.POST['password2']
        print(username2,email2,password2)
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def create_normaluser(request):
    if request.method == "POST":
        username3 = request.POST['username3']
        email3 = request.POST['email3']
        password3 = request.POST['password3']
        print(username3,email3,password3)
        return redirect('/')
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")