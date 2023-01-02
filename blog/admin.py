from django.contrib import admin
from .models import *

admin.site.register(Category)
# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title',"category",'user','created_at','updated_at']

