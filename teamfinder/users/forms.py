from django import forms

from .models import User
from .validators import validate_phone, validate_github_url


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["name", "surname", "email", "password"]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "surname", "avatar", "about", "phone", "github_url"]

    def clean_phone(self):
        return validate_phone(self.cleaned_data.get("phone"))

    def clean_github_url(self):
        return validate_github_url(self.cleaned_data.get("github_url"))