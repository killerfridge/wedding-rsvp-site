from django import forms
from .models import Guest, User
from django.forms.models import inlineformset_factory
from django.forms.widgets import Input
from crispy_forms.helper import FormHelper


class RSVPForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Guest
        fields = [
            'attending',
            'starter',
            'main',
            'dessert',
            'dietary',
            'id',
        ]


RSVPFormset = inlineformset_factory(
    User,
    Guest,
    fields=('attending', 'starter', 'main', 'dessert', 'child_starter', 'child_main', 'child_dessert', 'dietary', 'id'),
    can_delete=False,
    extra=0,
)
