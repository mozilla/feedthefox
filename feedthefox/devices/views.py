from django.shortcuts import render


def devices(request):
    return render(request, 'devices.jinja')


def device(request):
    return render(request, 'device.jinja')
