from django.forms import ModelForm

from .models import PeopleReg


class RegistrationToEventForm(ModelForm):
    class Meta:
        model = PeopleReg
        fields = ['event', 'name', 'email', 'phone']