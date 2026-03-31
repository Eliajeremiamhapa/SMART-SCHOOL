from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Certificate
from PIL import Image, ImageDraw, ImageFont
from django.contrib.staticfiles import finders
import io

# 1. View ya kuonesha orodha ya vyeti vyote
def certificate_list(request):
    certs = Certificate.objects.all()
    return render(request, 'certificates/list.html', {'certs': certs})

# 2. View ya kutengeneza picha ya cheti
def generate_certificate(request, cert_id):
    # Pata taarifa za cheti kutoka DB kwa kutumia certificate_id (siyo primary key)
    cert = get_object_or_404(Certificate, certificate_id=cert_id)
    
    # Tafuta Path ya picha na font kwenye static folders
    template_path = finders.find('certificates/images/template.png')
    font_path = finders.find('certificates/fonts/arial.ttf')

    if not template_path or not font_path:
        return HttpResponse(
            "Error: Faili la template.png au arial.ttf halijapatikana kwenye static/certificates/!", 
            status=404
        )

    try:
        # Fungua Picha ya Cheti
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        W, H = img.size 

        # Set Font (Ukubwa 60)
        font = ImageFont.truetype(font_path, 60)

        # Jina la Mpokeaji - Piga hesabu ya kuweka KATIKATI (Center)
        name_text = str(cert.recipient_name).upper() # Herufi kubwa zinapendeza zaidi
        name_bbox = draw.textbbox((0, 0), name_text, font=font)
        name_w = name_bbox[2] - name_bbox[0]
        draw.text(((W - name_w) / 2, 400), name_text, fill="black", font=font)

        # Jina la Kozi
        course_text = f"Successfully completed {cert.course_name}"
        course_bbox = draw.textbbox((0, 0), course_text, font=font)
        course_w = course_bbox[2] - course_bbox[0]
        draw.text(((W - course_w) / 2, 550), course_text, fill="blue", font=font)

        # Save picha kwenye memory (Buffer)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        
        return HttpResponse(buffer.getvalue(), content_type="image/png")
        
    except Exception as e:
        return HttpResponse(f"Kuna tatizo limetokea: {str(e)}", status=500)