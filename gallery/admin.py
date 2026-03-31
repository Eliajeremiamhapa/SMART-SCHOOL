from django.contrib import admin
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # list_display inasaidia kuona taarifa hizi kwenye meza ya admin panel
    list_display = ('title', 'is_public', 'created_at')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # Hapa tunaonyesha albamu, mwanafunzi husika, na muda picha ilipopakiwa
    list_display = ('album', 'student', 'uploaded_at')