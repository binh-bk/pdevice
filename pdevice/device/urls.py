from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('sample/', views.sample, name='sample'),
    path('<int:device_id>/detail/', views.detail, name='detail')
]
