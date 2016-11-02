from django.shortcuts import render

def index(request):
    """The home page for Citation Manager."""
    return render(request, 'citations/index.html')
