from django.shortcuts import render
from .models import *

# Create your views here.

def user_login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')

def show_all_blogs(request):  
    return render(request,'show_all_blogs.html')

def get_blog(request,id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id = id)
        context['blog'] = blog_obj
        

    except:
        pass    


    return render(request , 'detail_blog.html',context)