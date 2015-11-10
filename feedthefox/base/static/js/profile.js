jQuery(document).ready(function ($) {
    'use strict';

    var t = $('#id_device_info-imei');
    t.bind('propertychange keyup input paste', function(event) {
        var target = $('.imei-tos');
        var term = t.val();
        (term !== '' ? $(target).show('fast') : $(target).hide('fast'));
    });

    if ($('#DeviceModal .errorlist').length > 0) {
        $('#DeviceModal').modal('show');
    }
});
