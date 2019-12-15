from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from check_in_out.models import CheckTime
from manager_user.models import ManagerWorkers

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    current_user =  request.GET.get("current_user", request.user.get_username())

    return render(request, 'names/query.html',
           {
               'query': CheckTime.objects.filter(name_text=current_user),
               'workers': ManagerWorkers.objects.filter(manager_name=request.user.get_username()),
               'current_user': current_user
           })
