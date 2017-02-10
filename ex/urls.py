from django.conf.urls import url
from django.contrib.flatpages.views import flatpage
from django.views.generic import TemplateView

from . import views

app_name = 'ex'

urlpatterns = [
    url(r'^$', views.start_page, name='about'),
    url(r'^excursions/$', views.excursions, name='excursions'),
    url(r'^excursions/(?P<slug>[\S]+)/$', views.excursions, name='excursions'),
    url(r'^registration$', views.reg, name='registration'),
    url(r'^reviews$', views.add_review, name='reviews'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^blog/(?P<pk>[\d]+)/$', views.post_view, name='post'),
    url(r'^like_post/$', views.like_post, name='like_post'),
    url(r'^about-me/$', flatpage, {'url': '/about-me/'}, name='about-me'),
    url(r'^registration/success/$', TemplateView.as_view(template_name='ex/success.html'), name='success')
]
"""
url(r'^/registration$', ),
url(r'^/registration-individual$', ),
url(r'^/contacts$', ),
"""

