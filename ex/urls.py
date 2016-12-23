from django.conf.urls import url
from . import views

app_name = 'ex'

urlpatterns = [
    url(r'^$', views.start_page, name='about'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^excursions/(?P<slug>[\S]+)/$', views.excursions, name='excursions'),
    url(r'^events$', views.events, name='events'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^registration$', views.reg, name='registration'),
]
"""
url(r'^/registration$', ),
url(r'^/registration-individual$', ),
url(r'^/reviews$', ),
url(r'^/contacts$', ),
"""

