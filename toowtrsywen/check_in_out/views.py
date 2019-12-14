from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_text(request):
    return HttpResponse("Hello, world. You're at the polls index.")
