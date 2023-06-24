
from django.shortcuts import render
from .forms import HiddenImageForm
from .models import HiddenImage
from django.views import View
from stegano import lsb
from django.db.models import F
import os
from django.conf import settings


def home(request):
    return render(request, 'Api_documentation/base.html')


class HideMessageView(View):
    def get(self, request):
        form = HiddenImageForm()
        return render(request, 'Api_documentation/hide.html', {'form': form})

    def post(self, request):
        form = HiddenImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            hidden_text = request.POST.get('text')

            hidden_image = HiddenImage(image=image_file, text=hidden_text)
            hidden_image.save()

            encrypted_image = lsb.hide(
                hidden_image.image.path, hidden_image.text)
            encrypted_image_path = 'hidden_images/encrypted_image_{}.png'.format(
                hidden_image.id)
            encrypted_image.save(os.path.join(
                settings.MEDIA_ROOT, encrypted_image_path))

            hidden_image.encrypted_image_path = encrypted_image_path
            hidden_image.save()

            HiddenImage.objects.update(
                num_encrypted_images=F('num_encrypted_images') + 1)

            return render(request, 'Api_documentation/success.html')
        else:
            return render(request, 'Api_documentation/hide.html', {'form': form})


def decrypt(request):
    if request.method == 'POST' and 'image' in request.FILES:
        uploaded_file = request.FILES['image']
        decoded_message = lsb.reveal(uploaded_file)
        return render(request, "Api_documentation/decrypt.html", {'decrypt': decoded_message})
    else:
        return render(request, "Api_documentation/decrypt.html")
