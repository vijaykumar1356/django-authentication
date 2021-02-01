from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser
from .validators import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')

    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if not user:
    #             raise forms.ValidationError("This user does not exist")
    #         if not user.check_password(password):
    #             raise forms.ValidationError("Incorrect Password")
    #         if not user.is_active:
    #             raise forms.ValidationError("User is not Active")
    #     return super(LoginForm, self).clean(*args, **kwargs)



class RegisterForm(forms.Form):
    username = forms.CharField(validators=[username_length, username_is_alphanum, username_lowercase])
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'password'}), validators=[validate_password])
    re_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'repeat password'}))


    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if cleaned_data.get('password') != cleaned_data.get('re_password'):
            raise forms.ValidationError("Passwords should match!")
        return

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if user is not None:
            raise ValidationError("Username is taken!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        if user is not None:
            raise ValidationError("Account exists with this email already!")
        return email
