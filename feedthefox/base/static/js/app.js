jQuery(document).ready(function ($) {
    'use strict';

    $('#device-not').click(function() {
        var target = $('.device-not-options');
        $(this).hide();
        target.slideDown();
        $('html, body').animate({
            show: target,
            scrollTop: $(target).offset().top
        }, 2000);
    });
});
