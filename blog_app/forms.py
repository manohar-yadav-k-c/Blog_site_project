from django import forms
from .models import user_model,post_model
from django.contrib.auth.models import User

class user_form(forms.ModelForm):
    username=forms.CharField(help_text=None)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password','confirm_password')

class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields='__all__'


