from django.shortcuts import render

import django_filters

from feedthefox.devices.models import Device


class DeviceFilter(django_filters.FilterSet):
    type = django_filters.AllValuesFilter()
    manufacturer = django_filters.AllValuesFilter()

    class Meta:
        model = Device
        fields = ['manufacturer', 'type']

    def __init__(self, *args, **kwargs):
        super(DeviceFilter, self).__init__(*args, **kwargs)

        # Add "Any" entry to choice fields.
        for name, f in self.filters.items():
            if isinstance(f, django_filters.ChoiceFilter):
                f.field.choices = tuple([("", "Any"), ] + list(f.field.choices))


def devices(request):
    f = DeviceFilter(request.GET, queryset=Device.objects.all())
    return render(request, 'devices.html', {'device_filter': f})


def device(request):
    return render(request, 'device.html')
