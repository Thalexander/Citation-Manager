from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Citation
from .forms import CitationForm

def index(request):
    """The home page for Citation Manager."""
    return render(request, 'citations/index.html')

@login_required
def citations(request):
    """Show all citations."""
    citations = Citation.objects.filter(owner=request.user)
    context = {'citations': citations}
    return render(request, 'citations/citations.html', context)

@login_required
def new_citation(request):
    """Add a new citation."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CitationForm()
    else:
        # POST data submitted; process data.
        form = CitationForm(request.POST)
        if form.is_valid():
            new_citation = form.save(commit=False)
            new_citation.owner = request.user
            new_citation.save()
            return HttpResponseRedirect(reverse('citations:citations'))

    context = {'form': form}
    return render(request, 'citations/new_citation.html', context)

@login_required
def edit_citation(request, citation_id):
    """Edit an existing citation."""
    citation = Citation.objects.get(id=citation_id)
    if citation.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = CitationForm(instance=citation)
    else:
        # POST data submitted; process data.
        form = CitationForm(instance=citation, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('citations:citations'))

    context = {'citation': citation, 'form': form}
    return render(request, 'citations/edit_citation.html', context)
