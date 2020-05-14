from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from django.db import models
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from mptt.fields import TreeForeignKey

from content import models
from home.models import UserProfile

from content.models import Content, Category


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir')
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'country'}),
            'image': FileInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'image'}),
        }


class AddNewTrip(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('category', 'title', 'keywords', 'description', 'image', 'detail', 'slug', 'parent')
        widgets = {
            #'category': models.ForeignKey(Category, on_delete=models.CASCADE),
            'title': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'description'}),
            'status': TextInput(attrs={'size': '100', 'class': 'input',  'value': 'False'}),
            'image': FileInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'image'}),
            'slug': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'slug'}),
            #'parent': TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE),

        }


class AddNewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'keywords', 'description', 'image', 'slug', 'parent')
        widgets = {
            'title': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'description'}),
            'status': TextInput(attrs={'size': '100', 'class': 'input',  'value': 'False'}),
            'image': FileInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'image'}),
            'slug': TextInput(attrs={'size': '100', 'class': 'input', 'placeholder': 'slug'}),
        }
