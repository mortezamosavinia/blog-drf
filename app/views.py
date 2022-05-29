from django import forms
from django.shortcuts import render,redirect

from .models import Blog
from .forms import BlogForm

from django.http import HttpResponse
from .forms import signupform

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

@login_required(login_url='hlogin')
def index(request):
    return render(request,"index.html")

@login_required(login_url='hlogin')
def Allow(request):
    if request.method =='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(read)

    else:
        form = BlogForm(request.FILES)
    return render(request,'input.html',{"form":form})

@login_required(login_url='hlogin')
def read(request):
    read = Blog.objects.all()[::-1]
    return render(request,'read.html',{"read":read})

@login_required(login_url='hlogin')
def Update(request,id):
    upd = Blog.objects.get(id=id)
    update = BlogForm(request.POST or None , request.FILES or None , instance=upd)
    if update.is_valid():
        update.save()
        return redirect (read)
    return render(request,"update.html",{"update":update})

@login_required(login_url='hlogin')
def Delete(request,id):
    del_t=Blog.objects.get(id=id)    
    del_t.delete()
    return redirect(read)


def signup(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valid():
                form.save()

                user =request.POST.get('username')
                messages.success(request,"Account was craeted for user: "+ user)
                return redirect(hlogin)

        else:
            form = signupform()
        return render(request,'signup.html',{"form":form})


def hlogin(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method =="POST":
            uname = request.POST.get('username')
            upass = request.POST.get('password')

            user = authenticate(request, username=uname , password = upass)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect(hlogin)
        else:       
            return render (request,'hlogin.html')


def logoutUser(request):
	logout(request)
	return redirect('hlogin')

