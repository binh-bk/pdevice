from django.shortcuts import render, HttpResponse
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    DeleteView
)

from .models import Device



# Create your views here.
def index(request):
    return HttpResponse('<h1>This is the index page</h1>')


def PostListView(ListView):
    model = Device
    template='device/index.html'
    context_of_name = 'devices'
    ordering = ['-updated']