from django import forms

from datetimewidget.widgets import DateTimeWidget

from .models import PeopleReg, Reviews, Excursion


class RegistrationToEventForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Excursion.objects.all(), label='Экскурсия')

    class Meta:
        model = PeopleReg
        fields = ['event', 'date', 'name', 'email', 'phone']
        dateTimeOptions = {
            'format': 'mm/dd/yyyy hh:ii',
        }
        widgets = {'date': DateTimeWidget(attrs={'id': "id_date"}, bootstrap_version=3, usel10n=False,
                                          options=dateTimeOptions)}


class ReviewForm(forms.ModelForm):
    event_date = forms.DateField(input_formats=['%d.%m.%Y', '%m/%d/%Y', '%m/%d/%y'],
                                 label='Дата посещения')

    class Meta:
        model = Reviews
        fields = ['excursion', 'event_date', 'text']
