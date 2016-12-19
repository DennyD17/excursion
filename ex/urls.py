from django.conf.urls import url
from . import views

app_name = 'ex'

urlpatterns = [
    url(r'^$', views.start_page, name='about'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^excursions/(?P<slug>[\S]+)/$', views.excursions, name='excursions'),
    url(r'^events$', views.events, name='events'),
]
"""
url(r'^/events$', ),
url(r'^/excursions$', ),
url(r'^/registration$', ),
url(r'^/registration-individual$', ),
url(r'^/reviews$', ),
url(r'^/contacts$', ),
"""

