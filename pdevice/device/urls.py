from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:device_id>/detail/', views.detail, name='detail'),
    path('<int:device_id>/update/', views.update, name='update'),
    path('sample/', views.sample, name='sample'),
    path('home2/', views.HomePageView.as_view(), name='home2'),
]
