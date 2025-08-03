from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)
    previous_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=4, blank=True, null=True)
    gpa = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'graduation_year']
    
    def __str__(self):
        return f"{self.degree} - {self.university}"