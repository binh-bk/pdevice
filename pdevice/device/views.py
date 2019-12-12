from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_list_or_404, render
from django.urls import reverse

from .models import Device


# Create your views here.
def index(request):
    recent_device = Device.objects.order_by('operated')[:5]
    context = {
        'recent_device': recent_device
    }
    return render(request, 'index.html', context)


def sample(request):
    return render(request, 'bail.html')


def detail(request, device_id):
    # text = f'Requesting detail for device {device_id}'
    # return HttpResponse(f'<h1> {text} </h1>')
    try:
        device = Device.objects.get(pk=device_id)
    except Device.DoesNotExist:
        raise Http404("Device does not existed")

    return render(request, 'detail.html', {'device': device})


def PostListView(ListView):
    model = Device
    template = 'device/index.html'
    context_of_name = 'devices'
    ordering = ['-updated']
