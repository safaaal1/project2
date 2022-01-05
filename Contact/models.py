from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField, TextField
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

