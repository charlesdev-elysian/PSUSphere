# studentorg/forms.py
from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'  # or specify fields: ['name', 'college', 'description']