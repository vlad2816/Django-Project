from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from .forms import HiddenImageForm


def home(request):
    return render(request, 'Api_documentation/base.html')


def hide_text(request):
    if request.method == 'POST':
        image = request.FILES['image']
        text = request.POST['text']
        form = HiddenImageForm(request.POST, request.FILES)
        if form.is_valid():
            hidden_image = form.save()

        img = Image.open(image)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', 14)
        text_x = 20
        text_y = 20

        text_width, text_height = draw.textsize(text, font=font)
        draw.rectangle((text_x, text_y, text_x + text_width,
                       text_y + text_height), fill='white')

        # Save the modified image
        img.save('hidden_text_image.jpg')

        return render(request, 'Api_documentation/result.html', {'hidden_image': hidden_image})
    else:
        form = HiddenImageForm()

    return render(request, 'Api_documentation/hide_text.html', {'form': form})
