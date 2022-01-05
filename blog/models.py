from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField, TextField
from django.db import models


class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(null=True,default=0)
    population = models.IntegerField(null=True,default=0)
    address = models.TextField(null=True,max_length=250)
    type = models.TextField(null=True,max_length=15)
    image = models.ImageField(upload_to="./static/images/",null=True,max_length=150)


class user(User):
    def __str__(self):
        return self.user.username
    pass


