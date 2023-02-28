from django import forms
from django.core.exceptions import ValidationError

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
