from django import forms
from . import models


class AddPageForm(forms.Form):
    title = forms.CharField(max_length=48, label="Full name", widget=forms.TextInput(attrs={"class": "form-input"}))
    slug = forms.SlugField(max_length=48)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(label="Publish", required=False, initial=True)
    cat = forms.ModelChoiceField(queryset=models.Category.objects.all(), empty_label="Category not chosen")
