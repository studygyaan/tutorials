from django.shortcuts import render
import qrcode
from qrcode.image.pil import PilImage
from PIL import Image
import io
import base64

from .forms import QRCodeForm

def generate_qrcode(request):
    qr_code_image = None

    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            text_data = form.cleaned_data['text_data']

            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_data)
            qr.make(fit=True)

            qr_code_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Create a BytesIO buffer to temporarily store the image
            buffer = io.BytesIO()
            qr_code_image.save(buffer, format="PNG")
            qr_code_image_data = base64.b64encode(buffer.getvalue()).decode()

    else:
        form = QRCodeForm()

    return render(request, 'generate_qrcode.html', {'form': form, 'qr_code_image_data': qr_code_image_data})
