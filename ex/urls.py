from django.conf.urls import url
from . import views

app_name = 'ex'

urlpatterns = [
    url(r'^$', views.start_page, name='about'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^excursions/(?P<slug>[\S]+)/$', views.excursions, name='excursions'),
    url(r'^registration$', views.reg, name='registration'),
    url(r'^reviews$', views.add_review, name='reviews'),
    url(r'^blog$', views.blog, name='blog'),

]
"""
url(r'^/registration$', ),
url(r'^/registration-individual$', ),
url(r'^/contacts$', ),
"""

