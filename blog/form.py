from django import forms
from.models import *
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
  class Meta:
    model= Blog
    fields = ['content']

     



