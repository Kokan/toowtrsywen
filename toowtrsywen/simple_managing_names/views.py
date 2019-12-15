from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import Group 

from .models import Person

# Create your views here.
def index_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    if Group.objects.get(name="manager") in request.user.groups.all():
        return HttpResponseRedirect('/manager') 

    return render(request, 'names/index.html', {'name_list': Person.objects.all()})

def add_new_name(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    if request.method == 'POST':
        new_name = request.POST.get("name", "")
        Person.objects.create(name=new_name)
        return HttpResponseRedirect('/')

    return render(request, 'names/person_form.html', {})

def delete_name(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    _id = request.POST.get("delete", "")
    
    Person.objects.filter(id=_id).delete()
    return HttpResponseRedirect('/')    
    

def search_name(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/admin')

    name = request.POST.get("search", "")
    return render(request, 'names/search.html', {'name': Person.objects.filter(name=name)})