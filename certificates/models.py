from django.db import models

class Certificate(models.Model):
    # Taarifa za mwanafunzi
    recipient_name = models.CharField(
        verbose_name="Jina la Mpokeaji", 
        max_length=100
    )
    course_name = models.CharField(
        verbose_name="Jina la Kozi", 
        max_length=150
    )
    certificate_id = models.CharField(
        verbose_name="ID ya Cheti", 
        max_length=50, 
        unique=True
    )
    issue_date = models.DateField(
        verbose_name="Tarehe ya Kutolewa",
        auto_now_add=True
    )

    # SEHEMU YA UPLOAD: Hapa ndipo Admin atapakia faili la cheti (PDF au Picha)
    # Tumeongeza null=True na blank=True ili kuzuia migongano na DB iliyopo
    certificate_file = models.FileField(
        verbose_name="Pakia Faili la Cheti", 
        upload_to='certificates/uploads/',
        null=True,
        blank=True,
        help_text="Pakia picha (PNG/JPG) au PDF ya cheti hapa"
    )

    # QR Code (Ikiandaliwa na mfumo au kupakiwa)
    qr_code = models.ImageField(
        verbose_name="QR Code",
        upload_to='qr_codes/', 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"Cheti cha {self.recipient_name} - {self.course_name}"