from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.forms.widgets import PasswordInput, TextInput


from django.forms import ModelForm
from . models import createNote


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
    




class CreateNoteForm(ModelForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            'required' : '',
            'name' : 'title',
            'id': 'title',
            'type':'text',
            'class' : 'form-control',
            'placeholder' :'enter title here',
            'maxlength' : '100',
            'minlength' : '1'
        })

        self.fields["description"].widget.attrs.update({
            'required' : '',
            'name' : 'description',
            'id': 'description',
            'type':'text',
            'class' : 'form-control',
            'placeholder' :'Enter description here',
            'maxlength' : '2000',
            'minlength' : '1'
        })


    class Meta:
        model = createNote
        fields = ['title','description']





