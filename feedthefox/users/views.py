from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from feedthefox.users import forms


@login_required
def view_profile(request):
    newsletter_form = forms.ReceiveNewsLetterForm(request.POST or None,
                                                  instance=request.user,
                                                  prefix='newsletter')
    device_info_form = forms.UserDeviceInfoForm(request.POST or None,
                                                prefix='device_info')

    if newsletter_form.is_valid() and 'newsletter' in request.POST:
        newsletter_form.save()
        return redirect('view_profile')

    if device_info_form.is_valid() and 'device_info' in request.POST:
        device_info = device_info_form.save(commit=False)
        device_info.user = request.user
        device_info.save()
        return redirect('view_profile')

    ctx = {
        'newsletter_form': newsletter_form,
        'device_info_form': device_info_form
    }

    return render(request, 'profile.html', ctx)
