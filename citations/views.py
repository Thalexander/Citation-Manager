from django.shortcuts import render

from .models import Citation

def index(request):
    """The home page for Citation Manager."""
    return render(request, 'citations/index.html')

def citations(request):
    """Show all citations."""
    citations = Citation.objects.all()
    context = {'citations': citations}
    return render(request, 'citations/citations.html', context)
