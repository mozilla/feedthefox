from django import forms

from feedthefox.devices.models import DeviceInfo
from feedthefox.users.models import User


class ReceiveNewsLetterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['receive_newsletter', 'foxfooding_interest']


class UserDeviceInfoForm(forms.ModelForm):

    class Meta:
        model = DeviceInfo
        fields = ['device', 'imei']
