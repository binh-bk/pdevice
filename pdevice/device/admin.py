from django.contrib import admin

# Register your models here.
from .models import Device


admin.site.site_header = "Device Admin"
admin.site.site_title = "Manage Device"
admin.site.index_title = "Welcome to the Device Admin"


# class DeviceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['name']}),
#         ('_id', {'fields': ['updated'], 'class': ['collapse']}),
#     ]


# admin.site.register(Device, DeviceAdmin)

admin.site.register(Device)
