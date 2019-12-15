from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from check_in_out.models import CheckTime

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    return render(request, 'names/query.html', {'query': CheckTime.objects.filter(name_text=request.user.get_username())})