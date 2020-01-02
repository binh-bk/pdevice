from django.urls import path
from . import views

app_name = 'device'

urlpatterns = [
    path('', views.index, name='device-index'),
    # path('<int:device_id>/detail/', views.detail, name='detail'),
    path('<int:pk>/',
         views.DeviceDetailView.as_view(), name='device-detail'),
    path('new/',
         views.DeviceCreateView.as_view(), name='device-create'),
    path('<int:pk>/update/',
         views.DeviceUpdateView.as_view(), name='device-update'),
    path('<int:pk>/delete',
         views.DeviceDeleteView.as_view(), name='device-delete'),
    path('sample/', views.sample, name='device-sample'),
    path('home2/', views.HomePageView.as_view(), name='device-home2'),
    path('home3/', views.DevicePageView.as_view(), name='device-home3'),
    path('java/', views.javatest, name='java'),
    path('datetime/', views.datepick2, name='datepick'),
    path('datetime/post', views.get_datepick2, name='get_datepick2'),
    path('display/', views.display_date, name='display'),
]
