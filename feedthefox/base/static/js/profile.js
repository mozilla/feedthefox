jQuery(document).ready(function ($) {
    'use strict';

    var t = $('#imei-input');
    t.bind('propertychange keyup input paste', function(event) {
        var target = $('.imei-tos');
        var term = t.val();
        (term !== '' ? $(target).show() : $(target).hide());
    });

    if ($('#DeviceModal .errorlist').length > 0) {
        $('#DeviceModal').modal('show');
    }
});
