from .models import Post,Category
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class PostForm(ModelForm):
    class Meta:
        model=Post
        exclude=('author',)
    
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=200 )
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField()