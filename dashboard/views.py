from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from certificates.models import Certificate
from datetime import datetime
# from gallery.models import Photo # I-uncomment ukishatengeneza model ya Gallery

@login_required
def index(request):
    # 1. Kupata jina kamili la mtumiaji
    full_name = request.user.get_full_name() or request.user.username

    # 2. Kuchukua hesabu ya vyeti vya mwanafunzi huyu [cite: 15, 49]
    # Tunatumia __iexact ili kuzuia matatizo ya herufi kubwa/ndogo
    cert_count = Certificate.objects.filter(recipient_name__iexact=full_name).count()

    # 3. Salamu kulingana na muda (Extra UX touch)
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Habari za asubuhi"
    elif hour < 16:
        greeting = "Habari za mchana"
    else:
        greeting = "Habari za jioni"

    # 4. Context kwa ajili ya Template
    context = {
        'cert_count': cert_count,
        'username': request.user.username,
        'full_name': full_name,
        'greeting': greeting,
        'role': "Mwanafunzi", # Hii inaweza kuwa dynamic kulingana na Role [cite: 10]
    }
    
    return render(request, 'dashboard/index.html', context)