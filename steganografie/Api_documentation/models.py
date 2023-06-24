
from django.db import models


class HiddenImage(models.Model):
    image = models.ImageField(upload_to='hidden_images/')
    text = models.CharField(max_length=255)
    encrypted_image_path = models.CharField(
        max_length=255, blank=True, null=True)
    num_encrypted_images = models.PositiveIntegerField(default=0)
