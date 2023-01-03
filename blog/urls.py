from .views import *
from django.urls import path

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/',user_logout, name='user_logout'),
    path('', home),
    path('get-blog/<id>/', get_blog, name='get_blog'),
    path('show-all-blogs/', show_all_blogs, name='show_all_blogs'),
    path('create-blogs/', create_blogs, name='create_blogs'),
    path('delete-blogs/<id>/', delete_blogs, name='delete_blogs'),
    path('update-blogs/', update_blogs, name='update_blogs'),

]
