from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Muhimu kwa ajili ya settings.py
from django.conf.urls.static import static # Muhimu kwa ajili ya picha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),
    path('gallery/', include('gallery.urls')),
    path('certificates/', include('certificates.urls')), # Ongeza hii!
]

# Hii block hapa chini ndiyo inatatua tatizo la picha kutoonekana (Icon tu)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)