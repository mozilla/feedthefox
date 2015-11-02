from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def porting(request):
    return render(request, 'porting.html')


def devices(request):
    return render(request, 'devices.html')


def device(request):
    return render(request, 'device.html')


def custom_404(request):
    return HttpResponseNotFound(render(request, '404.html'))


def custom_500(request):
    return HttpResponseServerError(render(request, '500.html'))
