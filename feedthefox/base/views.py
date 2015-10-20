from django.shortcuts import render


def home(request):
    return render(request, 'home.jinja')


def devices(request):
    return render(request, 'devices.jinja')


def device(request):
    return render(request, 'device.jinja')
