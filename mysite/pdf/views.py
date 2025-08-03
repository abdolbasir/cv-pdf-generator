# views.py
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import ProfileModel
from .forms import ProfileForm

class ProfileCreateView(CreateView):
    model = ProfileModel
    form_class = ProfileForm
    template_name = 'pdf/profile_form.html'

class ProfileDetailView(DetailView):
    model = ProfileModel
    template_name = 'pdf/profile_detail.html'
    context_object_name = 'profile' 