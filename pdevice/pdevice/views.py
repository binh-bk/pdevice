from django.urls import path
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<h2>Main page: Under Construction</h2>')