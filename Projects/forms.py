from django import forms
from . import models
from django.utils.translation import gettext

field_attrs = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'description']
        labels = {
            'title': gettext('title'),
            'category': gettext('category'),
            'description': gettext('description'),
        }
        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'category': forms.Select(attrs=field_attrs),
            'description': forms.Textarea(attrs=field_attrs),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['title', 'category', 'status']
        labels = {
            'title': gettext('title'),
            'category': gettext('category'),
            'status': gettext('status'),
        }

        widgets = {
            'title': forms.TextInput(attrs=field_attrs),
            'category': forms.Select(attrs=field_attrs),
            'status': forms.Select(attrs=field_attrs),
        }
