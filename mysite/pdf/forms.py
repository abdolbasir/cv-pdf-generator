# forms.py
from django import forms
from .models import ProfileModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary', 'rows': 3}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University'}),
            'previous_work': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Previous Work Experience', 'rows': 3}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skills', 'rows': 3}),
        }
