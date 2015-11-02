from django import forms

from feedthefox.users.models import User


class ReceiveNewsLetterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['receive_newsletter']
