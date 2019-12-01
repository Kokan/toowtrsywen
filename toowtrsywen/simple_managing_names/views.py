from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import Person

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'names/index.html'
    context_object_name = 'name_list'

    def get_queryset(self):
        return Person.objects.all()

def add_new_name(request):
    if request.method == 'POST':
        new_name = request.POST.get("name", "")
        Person.objects.create(name=new_name)
        return HttpResponseRedirect('/names/')

    return render(request, 'names/person_form.html', {})

def delete_name(request):
    _id = request.POST.get("delete", "")
    #return render(request, 'names/thanks.html', {'name': _id})
    Person.objects.filter(id=_id).delete()
    return HttpResponseRedirect('/names/')    
    

def search_name(request):
    name = request.POST.get("search", "")
    return render(request, 'names/search.html', {'name': Person.objects.filter(name=name)})