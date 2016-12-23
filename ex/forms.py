from django import forms
from django.utils import timezone

from .models import PeopleReg, Event


class RegistrationToEventForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all().filter(starting__gte=timezone.now()).
                                   order_by('starting'))

    class Meta:
        model = PeopleReg
        fields = ['event', 'name', 'email', 'phone']
