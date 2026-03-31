import os
import io
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from .models import Certificate
from PIL import Image, ImageDraw, ImageFont
from django.contrib.staticfiles import finders  # Muhimu kwa Render

def certificate_list(request):
    certs = Certificate.objects.all()
    return render(request, 'certificates/list.html', {'certs': certs})

def generate_certificate(request, cert_id):
    cert = get_object_or_404(Certificate, certificate_id=cert_id)
    
    # MBINU YA RENDER: finders.find inatafuta popote static ilipo (hata staticfiles)
    template_path = finders.find('certificates/images/template.png')
    font_path = finders.find('certificates/fonts/arial.ttf')

    # Kama finders imefeli, tunajaribu kutafuta kwa mkono kwenye STATIC_ROOT
    if not template_path:
        template_path = os.path.join(settings.STATIC_ROOT, 'certificates', 'images', 'template.png')
    if not font_path:
        font_path = os.path.join(settings.STATIC_ROOT, 'certificates', 'fonts', 'arial.ttf')

    # Kama bado haionekani kabisa
    if not template_path or not os.path.exists(template_path):
        return HttpResponse(f"Error: Template haijapatikana hata kidogo!", status=404)

    try:
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        W, H = img.size 

        # Muhimu: Kama arial.ttf haipo, Pillow itatumia font ya mfumo isiyopendeza sana
        try:
            font = ImageFont.truetype(font_path, 60)
        except:
            font = ImageFont.load_default()

        # Jina la Mpokeaji
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