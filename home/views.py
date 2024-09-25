from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    """ View to return index page """
    return render(request, 'home/index.html', {
        'MEDIA_URL': settings.MEDIA_URL  # Pass MEDIA_URL to the template context
    })