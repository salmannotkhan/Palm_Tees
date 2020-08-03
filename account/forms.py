from django import forms
from .models import User, Address
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(forms.Form):
    
    email = forms.EmailField(widget=forms.EmailInput())
    
    password = forms.CharField(widget=forms.PasswordInput())

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
            'pattern': '^\w[a-z|A-Z]+$',
            'title': 'Enter valid first name',
            'autofocus':'',
            
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
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
    

class AddressCreateForm(forms.Form):
    """AddressCreate definition."""

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Name'
        }
    ))
    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Address'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'City'
        }
    ))
    state = forms.ChoiceField(choices=Address.STATE_LIST)
    pincode = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'placeholder': 'Pincode'
        }
    ))


    def save(self):
        if self.is_valid():
            return (Address.objects.create(
                name = self.cleaned_data['name'],
                address = self.cleaned_data['address'],
                city = self.cleaned_data['city'],
                state = self.cleaned_data['state'],
                pincode = self.cleaned_data['pincode']
                ))

    class Meta:
        model = Address
        fields = [
            'name',
            'address',
            'city',
            'state',
            'pincode',
        ]