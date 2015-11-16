from django.conf import settings
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views.static import serve


def home(request):
    return render(request, 'home.html')


def devices(request):
    return render(request, 'devices.html')


def device(request):
    return render(request, 'device.html')


def custom_404(request):
    return HttpResponseNotFound(render(request, '404.html'))


def custom_500(request):
    return HttpResponseServerError(render(request, '500.html'))


def contribute_view(request):
    """Serve a contribute.json file."""
    return serve(request, 'contribute.json', document_root=settings.BASE_DIR)
