import datetime
from .models import Device
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_list_or_404, render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.views.generic.edit import ModelFormMixin, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import jsonpickle

from bootstrap_datepicker_plus import DateTimePickerInput
# Create your views here.


def index(request):
    recent_device = Device.objects.order_by('operated')[:20]
    context = {
        'recent_device': recent_device
    }
    return render(request, 'index.html', context)


def javatest(request):
    device = Device.objects.order_by('operated')[5]
    districts = [{'name': 'Dong Da'},
                 {'name': 'Ba Dinh'},
                 {'name': 'Hoan Kiem'}

                 ]
    # context = {
    #     'device': jsonpickle.encode(device)
    # }
    context = {
        'device': districts
    }
    # print(device.name)
    return render(request, 'javatest.html', context)


def datepick(request):
    print('reach datepick request')
    return render(request, 'datetimepicker.html')


def get_datepick2(request):
    print(request.method)
    if request.method == 'post':
        date_dict = request.POST.dict()
        print(f'Request data: {date_dict}')
        # print(request.POST.get['start'])
        # print(request.POST.get['end'])
        return HttpResponse('This is a POST REQUEST')
    print('reach end request')
    return render(request, 'datetimepicker.html')


def display_date(request, start=0, end=0):
    context = {
        'start': start,
        'end': end
    }
    return render(request, 'displaydate.html', context)

def datepick2(request):
    print(request.method)
    if request.method == 'POST':
        data = request.POST.dict()
        try:
            start_ = datetime.datetime.strptime(
                data['start'], '%Y-%m-%d').date()
            end_ = datetime.datetime.strptime(data['end'], '%Y-%m-%d').date()
            print(data)
            # return HttpResponse(f'This is a POST REQUEST with {start_} and {end_}')
        except Exception as e:
            print(f'Error as {e}')
            return HttpResponse(f'Date is not understood {data}')
    print('reach datepick 2 request')
    return redirect('display')
    # return render(request, 'datefield.html')


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


class CreateView(CreateView):
    model = Device
    fields = '__all__'

    def get_form(self):
        form = super().get_form()
        form.fields['operated'] = DateTimePickerInput()
        return form


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

    def get_form(self):
        form = super().get_form()
        form.fields['operated'] = DateTimePickerInput()
        return form

    def form_valid(self, form):
        # form.instance.author = self.request.user
        return super().form_valid(form)


class DeviceUpdateView(UpdateView):

    model = Device
    fields = "__all__"
    template_name = 'form.html'

    def get_form(self):
        form = super().get_form()
        form.fields['operated'].wiget = DateTimePickerInput()
        return form

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
