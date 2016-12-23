from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404, Http404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

from .forms import RegistrationToEventForm
from . import models
from excursion import settings


def start_page(request):
    about = models.About.objects.all()[0]
    try:
        message = models.ImportantNote.objects.all()[0]
    except IndexError:
        return render(request, 'ex/main_page.html', {'about': about})
    return render(request, 'ex/main_page.html', {'message': message, 'about': about})


def excursions(request, slug=None):
    list_of_excursions = models.Excursion.objects.all()
    if slug == None:
        try:
            start_value = models.Excursion.objects.all()[0]
        except IndexError:
            return render(request, 'ex/excursions.html', {'Error_message': 'Извините, тут пока ничего нет'})
        else:
            events_for_excursion = models.Event.objects.all().filter(excursion=start_value.id,
                                                                     starting__gte=timezone.now()).order_by('starting')
            return render(request, 'ex/excursions.html', {'list_of_excursions': list_of_excursions,
                                                          'first': start_value, 'events': events_for_excursion})
    else:
        start_value = get_object_or_404(models.Excursion, slug=slug)
        events_for_excursion = models.Event.objects.all().filter(excursion=start_value.id,
                                                                 starting__gte=timezone.now()).order_by('starting')
        return render(request, 'ex/excursions.html', {'list_of_excursions': list_of_excursions, 'first': start_value,
                                                      'slug': slug, 'events': events_for_excursion})


def events(request):
    shedule = get_list_or_404(models.Event.objects.order_by('starting'), starting__gte=timezone.now())
    return render(request, 'ex/events.html', {'shedule': shedule})


def contacts(request):
    return render(request, 'ex/contacts.html', {'contacts': models.Contacts.objects.all()[0]})


def reg(request):
    if request.method == 'POST':
        form = RegistrationToEventForm(request.POST)
        if form.is_valid():
            form.save()
            mailto = form.cleaned_data.get('email')
            mes = form.cleaned_data.get('name') + \
                ', доброго времени суток! \nПоздравляю, вы успешно записаны на экскурсию ' + \
                str(form.cleaned_data.get('event'))
            send_mail('Запись на экскурсию', mes, settings.EMAIL_HOST_USER, ['Denis.Avramenko1705@gmail.com', mailto])
            return HttpResponseRedirect(reverse('ex:registration'))
    else:
        form = RegistrationToEventForm()
    people = models.PeopleReg.objects.all()
    return render(request, 'ex/registration.html', {'form': form, 'people': people})
