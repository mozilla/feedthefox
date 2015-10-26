from django.shortcuts import render


def home(request):
    return render(request, 'home.jinja')


def profile(request):
    return render(request, 'profile.jinja')


def gaia(request):
    return render(request, 'gaia.jinja')


def porting(request):
    return render(request, 'porting.jinja')


def b2gdroid(request):
    return render(request, 'b2gdroid.jinja')
