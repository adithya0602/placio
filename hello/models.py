from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    is_student=models.BooleanField('Is student',default=False)
    is_recruiter=models.BooleanField('Is recruiter',default=False)


class Sprofile(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    image=models.ImageField(default='api.jpg',upload_to='profile_images')

    def __str__(self):
        return f'{self.student.username}-profile'