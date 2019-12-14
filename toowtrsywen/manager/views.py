from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    return render(request, 'names/manager.html', {})