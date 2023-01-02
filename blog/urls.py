from .views import *
from django.urls import path

urlpatterns = [
    path('login/',user_login ,name='login'),
    path('register/',user_register, name='register'),
    path('',home),
    path('get_blog/<id>/',get_blog ,name='get_blog')
    
] 
