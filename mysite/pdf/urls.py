from django.urls import path
from . import views

urlpatterns = [
     path('profile/create/', views.ProfileCreateView.as_view(), name='create_profile'),
     path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),

]
