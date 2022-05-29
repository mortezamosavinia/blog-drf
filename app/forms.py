from datetime import date
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','descrip','image','date')

    title = forms.CharField(widget=forms.TextInput({"placeholder":"Enetr Title"}))
    descrip = forms.CharField(widget=forms.TextInput({"placeholder":"Enter Description"}))
    image = forms.ImageField()
    date = forms.DateField()

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",'email',"password1","password2",)
        

    username = forms.CharField()
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(),label="Confirm Password")
