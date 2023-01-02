from django.shortcuts import render
from .models import *

# Create your views here.

def get_blog(request,id):
    context = {}
    try:
        blog_obj = Blog.objects.get(id = id)
        context['blog'] = blog_obj
        

    except:
        pass    


    return render(request , 'detail_blog.html',context)