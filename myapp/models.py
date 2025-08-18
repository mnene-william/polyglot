from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__ (self):
        return self.name
