from email import message
from django.db import models

# Create your models here.

class ContactFrom(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.email