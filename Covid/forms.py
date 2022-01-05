
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blog.models import user
from django.forms import PasswordInput,SelectMultiple
from django.template.defaultfilters import slugify





class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control input-text'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control input-text'})
    

    class Meta:
        model = user
        fields = ['email','username','password1','password2',]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'Email Address'}),
            'username': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'Username'}),
        }



