from django.urls import path
from . import views

urlpatterns = [
     path('profile/create/', views.ProfileCreateView.as_view(), name='create_profile'),
     path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
     path('profile/<int:pk>/generate-pdf/', views.generate_pdf, name='generate_pdf'),
     path('profile/<int:pk>/generate-pdf-alt/', views.generate_pdf_alternative, name='generate_pdf_alternative'),
     path('profile/<int:pk>/debug-pdf/', views.test_pdf_generation, name='debug_pdf'),
]
