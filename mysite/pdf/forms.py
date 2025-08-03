# forms.py
from django import forms
from .models import ProfileModel, Education

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'email', 'phone', 'summary', 'previous_work', 'skills']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary', 'rows': 3}),
            'previous_work': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Previous Work Experience', 'rows': 3}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skills', 'rows': 3}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'university', 'graduation_year', 'gpa', 'description']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree (e.g., Bachelor of Science in Computer Science)'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'University Name'}),
            'graduation_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Graduation Year (e.g., 2023)'}),
            'gpa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GPA (e.g., 3.8/4.0)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional details about your education (optional)', 'rows': 2}),
        }

EducationFormSet = forms.inlineformset_factory(
    ProfileModel,
    Education,
    form=EducationForm,
    extra=1,
    can_delete=True,
    fields=['degree', 'university', 'graduation_year', 'gpa', 'description']
)
