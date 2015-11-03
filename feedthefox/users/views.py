from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from feedthefox.users import forms


@login_required
def view_profile(request):
    newsletter_form = forms.ReceiveNewsLetterForm(request.POST or None,
                                                  instance=request.user)

    if newsletter_form.is_valid():
        newsletter_form.save()
        return redirect('view_profile')

    data = {'newsletter_form': newsletter_form}
    return render(request, 'profile.html', data)
