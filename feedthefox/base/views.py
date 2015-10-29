from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def gaia(request):
    return render(request, 'gaia.html')


def porting(request):
    return render(request, 'porting.html')


def b2gdroid(request):
    return render(request, 'b2gdroid.html')


def devices(request):
    return render(request, 'devices.html')


def device(request):
    return render(request, 'device.html')
