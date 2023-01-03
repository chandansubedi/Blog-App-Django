from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username =request.POST.get('username')
        password =request.POST.get('password')
        user_obj =User.objects.filter(username = username)

        if  not user_obj.exists():
            messages.success(request,'user not found')
            return redirect('/login/')

        user_obj = authenticate(username = username, password = password)
        
        if not user_obj:
            messages.success(request,'incorrect username or password')
            return redirect('/login/')

        login(request , user_obj)
        return redirect('/')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')




def user_register(request):
    if request.method == "POST":
        username =request.POST.get('username')
        email =request.POST.get('email')
        password =request.POST.get('password')

        user_obj =User.objects.filter(username = username)
        if user_obj.exists():
            messages.success(request,'username is already taken')
            return redirect('/register/')

        user_obj =User.objects.filter(email = email)  
        if user_obj.exists():
            messages.success(request,'Email is already taken')
            return redirect('/register/')  

        user_obj=User(username = username , email = email) 
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request , 'Account created successfully ')
        return redirect('/login/')
        

 
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')

def show_all_blogs(request):  
    return render(request,'show_all_blogs.html')

def create_blogs(request):
    return render(request , 'create_blogs.html') 

def update_blogs(request):
    return render(request , 'update_blogs.html')  


def delete_blogs(request,id): 
    return redirect('/')



def get_blog(request,id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id = id)
        context['blog'] = blog_obj
        

    except:
        pass    


    return render(request , 'detail_blog.html',context)