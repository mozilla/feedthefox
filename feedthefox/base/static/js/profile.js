jQuery(document).ready(function ($) {
    'use strict';

    var t = $('#id_device_info-imei');
    t.bind('propertychange keyup input paste', function(event) {
        var target = $('.imei-tos');
        var group = $(this).parent('.form-group');
        var status = $('.imei-status');
        status.hide();
        var term = t.val();
        if (term !== '') {
            $(target).show('fast');
            $(status).show();
            $.ajax({
                url: "/imei/" + term,
                type: "GET",
                success: function(json) {
                    if (json.status) {
                        group.removeClass('has-error');
                        group.addClass('has-success');
                        $('#imei-submit').removeClass('disabled');
                        group.find('.errorlist').hide();
                        status.show();
                        status.addClass('fa-check');
                        status.removeClass('fa-times');
                        status.text(' valid');
                    } else {
                        group.removeClass('has-success');
                        group.addClass('has-error');
                        $('#imei-submit').addClass('disabled');
                        status.show();
                        status.addClass('fa-times');
                        status.removeClass('fa-check');
                        status.text(' invalid');
                    }
                },
                error: function() {
                    group.removeClass('has-success');
                    group.addClass('has-error');
                    $('#imei-submit').addClass('disabled');
                    status.show();
                    status.addClass('fa-times');
                    status.removeClass('fa-check');
                    status.text(' invalid');
                }
            });
        } else {
            $(target).hide('fast');
            $(status).hide();
            $('#imei-submit').removeClass('disabled');
        }
    });

    if ($('#DeviceModal .errorlist').length > 0) {
        $('#DeviceModal').modal('show');
    }

    $('#newsletter-form :checkbox').change(function(){
        $('#newsletter-form').submit();
    });

});
