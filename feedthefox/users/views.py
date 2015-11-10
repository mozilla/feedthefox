from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from feedthefox.devices.models import DeviceInfo
from feedthefox.users import forms


@login_required
def view_profile(request):
    newsletter_form = forms.ReceiveNewsLetterForm(request.POST or None,
                                                  instance=request.user,
                                                  prefix='newsletter')
    device_info_form = forms.UserDeviceInfoForm(request.POST or None,
                                                prefix='device_info')

    if 'device_info' in request.POST and device_info_form.is_valid():
        device_info = device_info_form.save(commit=False)
        device_info.user = request.user
        device_info.save()
        return redirect('view_profile')
    elif 'newsletter' in request.POST and newsletter_form.is_valid():
        newsletter_form.save()
        return redirect('view_profile')

    ctx = {
        'newsletter_form': newsletter_form,
        'device_info_form': device_info_form
    }

    return render(request, 'profile.html', ctx)


@login_required
def delete_device_info(request, id):
    device_info = get_object_or_404(DeviceInfo, pk=id)

    if not device_info.user == request.user:
        raise Http404

    device_info.delete()
    return redirect('view_profile')
