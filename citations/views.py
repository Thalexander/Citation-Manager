from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Citation
from .forms import CitationForm

def index(request):
    """The home page for Citation Manager."""
    return render(request, 'citations/index.html')

def citations(request):
    """Show all citations."""
    citations = Citation.objects.all()
    context = {'citations': citations}
    return render(request, 'citations/citations.html', context)


def new_citation(request):
    """Add a new citation."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CitationForm()
    else:
        # POST data submitted; process data.
        form = CitationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('citations:citations'))

    context = {'form': form}
    return render(request, 'citations/new_citation.html', context)
