"""Defines URL patterns for citaions."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Show all citations
    url(r'^citations/$', views.citations, name='citations'),

    # page for adding new citations
    url(r'^new_citation/$', views.new_citation, name='new_citation'),
]
