from django import forms
from .models import Guest, User
from django.forms.models import inlineformset_factory
from django.forms.widgets import Input


class RSVPForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = [
            'first',
            'last',
            'attending',
        ]


RSVPFormset = inlineformset_factory(
    User,
    Guest,
    fields=('attending', 'starter', 'main', 'dietary', 'id'),
    can_delete=False,
    extra=0,
)
