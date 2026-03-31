from django.db import models
from django.conf import settings

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # help_text imewekwa ndani ya mabano vizuri ili isilete error
    is_public = models.BooleanField(
        default=True, 
        help_text="Weka True kwa matukio ya shule, False kwa picha za mwanafunzi binafsi."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='school_gallery/')
    # ForeignKey inatumia settings.AUTH_USER_MODEL kuunganisha na User wa login app
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Picha kwenye {self.album.title}"