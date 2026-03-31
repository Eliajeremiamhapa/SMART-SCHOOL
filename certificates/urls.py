from django.urls import path
from . import views

urlpatterns = [
    # Hii itafungua cheti ukiandika mfano: /certificates/generate/CERT123/
    path('generate/<str:cert_id>/', views.generate_certificate, name='generate_certificate'),
    
    # Ukurasa wa kuona orodha ya vyeti (tutaandika HTML yake chini)
    path('list/', views.certificate_list, name='certificate_list'),
]