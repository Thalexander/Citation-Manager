"""Defines URL patterns for citaions."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all citations
    url(r'^citations/$', views.citations, name='citations'),
]
