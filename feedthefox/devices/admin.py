from django.contrib import admin

from feedthefox.devices.models import Build, Device, DeviceInfo


class DeviceInfoInline(admin.TabularInline):
    model = DeviceInfo
    extra = 1


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    inlines = (DeviceInfoInline,)
    list_display = ('model', 'manufacturer',)


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass
