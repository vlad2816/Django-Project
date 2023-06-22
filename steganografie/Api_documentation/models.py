
from django.db import models


class HiddenImage(models.Model):
    image = models.FileField(upload_to='hidden_images/')
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
