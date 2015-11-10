jQuery(document).ready(function ($) {
    $('#BuildModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var recipient = button.data('build');
        var modal = $(this)
        modal.find('#build-link').attr('href', recipient);
    });
});
