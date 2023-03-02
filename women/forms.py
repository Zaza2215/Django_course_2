from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from . import models


# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=48, label="Full name", widget=forms.TextInput(attrs={"class": "form-input"}))
#     slug = forms.SlugField(max_length=48)
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
#     is_published = forms.BooleanField(label="Publish", required=False, initial=True)
#     cat = forms.ModelChoiceField(queryset=models.Category.objects.all(), empty_label="Category not selected")

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category not selected"

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 36:
            raise ValidationError("Length more then 36 signs")

        return title

    class Meta:
        model = models.Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }
