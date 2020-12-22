from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Review

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfile(forms.ModelForm):
    full_name = forms.CharField(required=True)
    class Meta:
        model = UserProfile
        fields = ['full_name', 'profile_pic']


class AddReview(forms.ModelForm):
    review = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={'placeholder': 'Review'}))
    class Meta:
        model = Review
        fields = ['review']
