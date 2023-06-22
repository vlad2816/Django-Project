
from django.shortcuts import render
from .forms import HiddenImageForm
from stegano import exifHeader
from .models import HiddenImage
from django.views import View
from stegano import lsb


def home(request):
    return render(request, 'Api_documentation/base.html')


class HideMessageView(View):
    def get(self, request):
        form = HiddenImageForm()
        return render(request, 'hide.html', {'form': form})

    def post(self, request):
        form = HiddenImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES.get('image')
            hidden_text = request.POST.get('text')

            hidden_image = HiddenImage(image=image_file, text=hidden_text)
            hidden_image.save()

            encrypted_image = lsb.hide(
                hidden_image.image.path, hidden_image.text)
            encrypted_image.save(hidden_image.image.path)

            return render(request, 'success.html')
        else:
            return render(request, 'Api_documentation/hide.html', {'form': form})


def decrypt(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        decoded_message = str(exifHeader.reveal(uploaded_file))
        return render(request, "Api_documentation/decrypt.html", {'decrypt': decoded_message[1:]})
    else:
        return render(request, "Api_documentation/decrypt.html")
