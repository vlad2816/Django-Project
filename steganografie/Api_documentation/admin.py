

from django.contrib import admin
from .models import HiddenImage


class HiddenImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'encrypted_image_path',)
    list_display = ('id', 'image', 'text', 'num_encrypted_images')


admin.site.register(HiddenImage, HiddenImageAdmin)
