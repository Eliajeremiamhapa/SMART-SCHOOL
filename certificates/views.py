import os
import io
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import Certificate
from PIL import Image, ImageDraw, ImageFont

# 1. View ya kuonesha orodha ya vyeti
def certificate_list(request):
    certs = Certificate.objects.all()
    return render(request, 'certificates/list.html', {'certs': certs})

# 2. View ya kutengeneza picha ya cheti
def generate_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, certificate_id=cert_id)
    
    # MBINU MPYA: Badala ya finders, tunatumia BASE_DIR moja kwa moja
    # Hii inahakikisha Render haipotei njia
    template_path = os.path.join(settings.BASE_DIR, 'certificates', 'static', 'certificates', 'images', 'template.png')
    font_path = os.path.join(settings.BASE_DIR, 'certificates', 'static', 'certificates', 'fonts', 'arial.ttf')

    # Debug: Kama bado inakataa, itakuambia njia kamili inayotafuta
    if not os.path.exists(template_path) or not os.path.exists(font_path):
        return HttpResponse(
            f"Error: Mafaili hayajapatikana!<br>Inatafuta hapa: {template_path}", 
            status=404
        )

    try:
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        W, H = img.size 

        font = ImageFont.truetype(font_path, 60)

        # Kuweka Jina Katikati
        name_text = str(cert.recipient_name).upper()
        name_bbox = draw.textbbox((0, 0), name_text, font=font)
        name_w = name_bbox[2] - name_bbox[0]
        draw.text(((W - name_w) / 2, 400), name_text, fill="black", font=font)

        # Jina la Kozi
        course_text = f"Successfully completed {cert.course_name}"
        course_bbox = draw.textbbox((0, 0), course_text, font=font)
        course_w = course_bbox[2] - course_bbox[0]
        draw.text(((W - course_w) / 2, 550), course_text, fill="blue", font=font)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        
        return HttpResponse(buffer.getvalue(), content_type="image/png")
        
    except Exception as e:
        return HttpResponse(f"Kuna tatizo limetokea: {str(e)}", status=500)