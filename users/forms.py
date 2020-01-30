from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


class RegistrationForm(UserCreationForm):
    username =  forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email","password1","password2")

    def clean_username(self):
            username = self.cleaned_data['username']
            if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
                raise forms.ValidationError(u'Username "%s" is already in use.' % username)
            return username

    def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError('Email addresses must be unique.')
            return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]

        if commit:
            user.save()
        return user


