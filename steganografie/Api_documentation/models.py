from django.db import models

# Create your models here.


class Photo(models.Model):

    email = models.EmailField("Enter Email")
    file = models.FileField(upload_to="cache")
    message = models.CharField("Enter message", max_length=150, default="")
