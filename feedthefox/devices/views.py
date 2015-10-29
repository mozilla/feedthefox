from django.shortcuts import render


def devices(request):
    return render(request, 'devices.html')


def device(request):
    return render(request, 'device.html')
