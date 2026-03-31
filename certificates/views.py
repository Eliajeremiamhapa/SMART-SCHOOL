from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse, Http404
from .models import Certificate
import mimetypes

# 1. View ya kuonesha orodha ya vyeti (Haitabadilika sana)
def certificate_list(request):
    certs = Certificate.objects.all()
    return render(request, 'certificates/list.html', {'certs': certs})

# 2. View ya mwanafunzi kudownload faili aliloweka Admin
def generate_certificate(request, cert_id):
    # Pata cheti husika kwa ID
    cert = get_object_or_404(Certificate, certificate_id=cert_id)
    
    # Angalia kama Admin ameshapakia faili
    if not cert.certificate_file:
        return HttpResponse(
            "<h2>Samahani!</h2><p>Cheti chako bado hakijawekwa kwenye mfumo. Tafadhali wasiliana na Admin.</p>", 
            status=404
        )

    try:
        # Fungua faili kutoka kwenye Media Storage
        file_handle = cert.certificate_file.open('rb')
        
        # Tambua aina ya faili (PDF, PNG, au JPG) ili browser ijue jinsi ya ku-handle
        content_type, _ = mimetypes.guess_type(cert.certificate_file.name)
        
        # Mpe mwanafunzi faili lake
        response = FileResponse(file_handle, content_type=content_type)
        
        # Hii inamlazimisha browser i-download (attachment) badala ya kufungua tu
        response['Content-Disposition'] = f'attachment; filename="Cheti_{cert.certificate_id}.pdf"'
        
        return response

    except Exception as e:
        return HttpResponse(f"Kuna tatizo la kiufundi: {str(e)}", status=500)