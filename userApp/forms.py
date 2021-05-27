from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Email ',
                                                           'type': 'email',
                                                           'class': 'form-control', }))

    # just form design er Jonno . last a widget diye korte partam
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                                      'class': 'form-control', }))
    password1 = forms.CharField(required=True,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control', }))
    password2 = forms.CharField(required=True,
                                label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password confirmation',
                                                                  'class': 'form-control', }))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class profile_Edit(forms.ModelForm):
    class Meta:
        model = UserProfile()
        exclude = ('user',)
