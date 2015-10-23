from django.shortcuts import render


def home(request):
    return render(request, 'home.jinja')


def devices(request):
    return render(request, 'devices.jinja')
def profile(request):
    return render(request, 'profile.jinja')


def device(request):
    return render(request, 'device.jinja')


def porting(request):
    return render(request, 'porting.jinja')


def b2gdroid(request):
    return render(request, 'b2gdroid.jinja')
