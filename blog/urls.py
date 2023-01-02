from .views import *
from django.urls import path

urlpatterns = [
    path('get_blog/<id>/',get_blog ,name='get_blog')
    
]
