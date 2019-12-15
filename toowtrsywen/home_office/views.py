from django.shortcuts import render
from django.http import HttpResponse

from .models import HomeOfficeRequest

# Create your views here.
def homeoffice_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    return render(request, 'names/home_office.html', {'homeoffice_form': HomeOfficeRequest.objects.filter(name=request.user.get_username())})