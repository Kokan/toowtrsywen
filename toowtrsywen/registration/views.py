from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .models import Person

# Create your views here.
class RegistrationView(generic.ListView):
    template_name = 'registration/registration.html'
    context_object_name = 'name_list'

    def get_queryset(self):
        return Person.objects.all()

def register(request):
    if request.method == 'POST':
        new_name = request.POST.get("name", "")
        new_email = request.POST.get("email", "")
        new_password = request.POST.get("password", "")
        Person.objects.create(name=new_name, email=new_email, password=new_password)
        return HttpResponseRedirect('/registration/')

    return render(request, 'registration/registration.html', {})
