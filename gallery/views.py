from django.shortcuts import render, get_object_or_404
from .models import Album
from django.contrib.auth.decorators import login_required

@login_required
def gallery_list(request):
    # Anaona albamu za shule (Public)
    albums = Album.objects.filter(is_public=True)
    return render(request, 'gallery/list.html', {'albums': albums})

@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    # Lazy Loading: Picha zitapakiwa kadiri mtumiaji anavyozihitaji [cite: 56, 57]
    photos = album.photos.all()
    return render(request, 'gallery/detail.html', {'album': album, 'photos': photos})