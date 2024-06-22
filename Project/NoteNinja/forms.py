from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django import forms

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' : '',
            'name' : 'username',
            'id': 'username',
            'type':'text',
            'class' : 'form-control',
            'placeholder' :'Enter username',
            'maxlength' : '20',
            'minlength' : '5'
        })


        self.fields["email"].widget.attrs.update({
            'required' : '',
            'name' : 'email',
            'id': 'email',
            'type':'email',
            'class' : 'form-control',
            'placeholder' :'Email-id',
            'maxlength' : '30',
            'minlength' : '5'
        })


        self.fields["password1"].widget.attrs.update({
            'required' : '',
            'name' : 'password1',
            'id': 'password1',
            'type':'password',
            'class' : 'form-control',
            'placeholder' :'Password',
            'maxlength' : '16',
            'minlength' : '8'
        })


        self.fields["password2"].widget.attrs.update({
            'required' : '',
            'name' : 'password2',
            'id': 'password2',
            'type':'password',
            'class' : 'form-control',
            'placeholder' :'Confirm Password',
            'maxlength' : '16',
            'minlength' : '8'
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' : '',
            'name' : 'username',
            'id': 'username',
            'type':'text',
            'class' : 'form-control',
            'placeholder' :'Enter username',
            'maxlength' : '20',
            'minlength' : '5'
        })

        self.fields["password"].widget.attrs.update({
            'required' : '',
            'name' : 'password',
            'id': 'password',
            'type':'password',
            'class' : 'form-control',
            'placeholder' :'Password',
            'maxlength' : '16',
            'minlength' : '8'
        })

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    




