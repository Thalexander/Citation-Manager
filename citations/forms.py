from django import forms

from .models import Citation

class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation
        fields = ['title','link','note']
        labels = {'title': 'Title',
                  'link': 'URL',
                  'note': 'Note'
                 }
