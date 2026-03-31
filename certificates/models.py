from django.db import models

class Certificate(models.Model):
    # Tumia verbose_name badala ya max_material
    recipient_name = models.CharField(verbose_name="Jina la Mpokeaji", max_length=100)
    course_name = models.CharField(max_length=150)
    issue_date = models.DateField(auto_now_add=True)
    certificate_id = models.CharField(max_length=50, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"Cheti cha {self.recipient_name} - {self.course_name}"