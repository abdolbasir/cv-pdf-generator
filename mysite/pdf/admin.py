from django.contrib import admin
from .models import ProfileModel, Education

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(Education)