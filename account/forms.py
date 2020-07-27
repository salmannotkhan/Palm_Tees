from django import forms
from .models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
      
    class Meta: 
        model = User
        fields =[
            'email',
            'password'
        ]

class UserSignupForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'pattern': '^\w[a-z|A-Z]+$',
            'title': 'Enter valid first name',
            'autofocus':'',
            
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'pattern': '^\w[a-z|A-Z]+$',
            'title': 'Enter valid last name'
        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'pattern': '[9|8|7|6]\d{9}',
            'title': 'Enter valid mobile number'
        }
    ))

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name in ('password1', 'password2'):
                visible.field.widget.attrs['autocomplete'] = 'new-password'
            elif visible.name == 'email':
                visible.field.widget.attrs['autocomplete'] = 'off'

            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'phone', 
            'email',
            'password1', 
            'password2', 
            ]
    