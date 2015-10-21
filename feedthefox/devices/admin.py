from django.contrib import admin

from feedthefox.devices.models import Build, Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer',)


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass
