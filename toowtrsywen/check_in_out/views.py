from django.shortcuts import render
from django.http import HttpResponse
from .models import CheckTime
from .serializers import CheckTimeSerializer
from rest_framework import viewsets
# Create your views here.
class CheckTimeView(viewsets.ModelViewSet):
    queryset = CheckTime.objects.all()
    #queryset = CheckTime.objects.create(name_text='testjani',in_or_out='in')
    serializer_class = CheckTimeSerializer

def main_text(request):
    # CheckTime.objects.create(name_text='testjani',in_or_out='in')
    return HttpResponse("Added.")
