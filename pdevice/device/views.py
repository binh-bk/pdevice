from .models import Device
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def index(request):
    recent_device = Device.objects.order_by('operated')[:20]
    context = {
        'recent_device': recent_device
    }
    return render(request, 'index.html', context)


def detail(request, device_id):
    # text = f'Requesting detail for device {device_id}'
    # return HttpResponse(f'<h1> {text} </h1>')
    try:
        device = Device.objects.get(pk=device_id)
    except Device.DoesNotExist:
        raise Http404("Device does not existed")

    return render(request, 'detail.html', {'device': device})


def update(request, device_id):
    try:
        device = Device.objects.get(pk=device_id)
    except Device.DoesNotExist:
        raise Http404("Device does not existed")

    return render(request, 'detail.html', {'device': device})


def sample(request):
    return render(request, 'bail.html')

# Edit a post
# def edit(request, pk, template_name='Crud/edit.html'):
#     post= get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, template_name, {'form':form})


def PostListView(ListView):
    model = Device
    template = 'device/index.html'
    context_of_name = 'devices'
    ordering = ['-updated']


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_device'] = Device.objects.all()[:5]
        return context


class DevicePageView(ListView):

    model = Device
    template_name = 'index.html'
    context_object_name = 'recent_device'
    ordering = ['-operated']


class DeviceDetailView(DetailView):

    model = Device
    template_name = 'detail.html'


class DeviceCreateView(CreateView):

    model = Device
    fields = "__all__"
    template_name = 'form.html'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


class DeviceUpdateView(UpdateView):

    model = Device
    fields = "__all__"
    template_name = 'form.html'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


class DeviceDeleteView(DeleteView):

    model = Device
    success_url = '/device'
    fields = "__all__"
    template_name = 'delete.html'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)
