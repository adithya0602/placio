from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student=models.BooleanField('Is student',default=False)
    is_recruiter=models.BooleanField('Is recruiter',default=False)