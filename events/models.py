from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Events(models.Model):
    img = models.ImageField(upload_to='pics')
    event = models.CharField(max_length=100)
    desc = models.TextField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    gform_link = models.TextField()


class Mainbanner(models.Model):
    eventimg = models.ImageField(upload_to='pics')
    eventName = models.CharField(max_length=100)
    eventdesc = models.TextField()
