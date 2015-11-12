from django.contrib import admin

from feedthefox.devices.models import Build, Device, DeviceInfo


@admin.register(DeviceInfo)
class DeviceInfoAdmin(admin.ModelAdmin):
    list_display = ('get_mozillian_username', 'device', 'imei',)

    def get_mozillian_username(self, obj):
        return obj.user.mozillian_username
    get_mozillian_username.short_description = 'Mozillian Username'
    get_mozillian_username.admin_order_field = 'user__first_name'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer',)


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass
