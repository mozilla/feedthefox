jQuery(document).ready(function ($) {
    'use strict';

    // Bug type toggle
    $('.bug-type').on('click', function(e) {
        e.preventDefault();
        var firstchoice = $(this);
        var secondchoice = $(this).siblings();
        firstchoice.addClass('active');
        secondchoice.removeClass('active');
        $(firstchoice.data('target')).show();
        $(secondchoice.data('target')).hide();
    });

    var escapeHTML = function(str) {
      return str.replace(/&/g, '&amp;')
                .replace(/>/g, '&gt;')
                .replace(/</g, '&lt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#39;')
                .replace(/`/g, '&#96;');
    };

    // Fetch bugs and metadata
    var bz = {
        searchBugs: function(data) {
            var url = 'https://bugzilla.mozilla.org/rest/bug';
            var opts = {
                url: url,
                data: data
            };
            return $.ajax(opts, function() {}, function(error) {
                console.error('Error fetching', error);
            });
        },
        fetchComments: function(data) {
            var url = 'https://bugzilla.mozilla.org/rest/bug/' + data.id + '/comment';
            var opts = {
                url: url,
                data: data
            };
            return $.ajax(opts, function() {}, function(error) {
                console.error('Error fetching', error);
            });
        }
    };

    // Initiate popover
    $('body').on('bugsloaded', function() {
        var popovers = $('[data-toggle="popover"]');
        popovers.popover();
        popovers.on('show.bs.popover', function(e) {
            var id = parseInt($(this).data('id'));
            popovers.not(`[data-id="${id}"]`).popover('hide');
            if ($(this).data('loaded')) {
                return;
            }
            var self = this;
            bz.fetchComments({
                id: id
            }).done(function(data) {
                var bugLink = `https://bugzilla.mozilla.org/show_bug.cgi?id=${id}`;
                var voteLink = `https://bugzilla.mozilla.org/page.cgi?id=voting/user.html&bug_id=${id}#vote_${id}`;
                var text = data.bugs[id].comments[0].text;
                text = text.replace(/\n/g, '<br>');
                text += `<br><br>
                         <a href="${bugLink}" target="_blank">See More</a> |
                         <a href="${voteLink}" target="_blank">Vote</a>`;
                $(self).attr('data-loaded', true);
                $(self).attr('data-content', text);
                $(self).popover('show');
            });
        });
    });

    // Filter
    $('body').on('keyup', '#bug-filter', function() {
         var target = $('.bugs-tbody');
         var rex = new RegExp($(this).val(), 'i');
         var bugs = target.find('tr');
         bugs.hide();
         bugs.filter(function() {
             return rex.test($(this).text());
         }).show();
    });

    // Render all bugs
    var render = function(params) {
        var elements = '';
        var maxVotes = 0;
        params.bugs.forEach(function(bug) {
            if (bug.votes > maxVotes) {
                maxVotes = bug.votes;
            }
        });

        params.bugs.forEach(function(bug) {
            var bugLink = `https://bugzilla.mozilla.org/show_bug.cgi?id=${bug.id}`;
            var voteLink = `https://bugzilla.mozilla.org/page.cgi?id=voting/user.html&bug_id=${bug.id}#vote_${bug.id}`;
            var element = `
              <tr>
                <td class="text-center hidden-xs">
                  <strong><a href="${bugLink}" target="_blank">#${bug.id}</a></strong>
                </td>
                <td colspan="5">
                  <a data-toggle="popover" data-placement="auto" title="<a
                     href='${bugLink}' target='_blank'>Bug ${bug.id}</a> -
                     ${escapeHTML(bug.summary)} (${bug.votes} Votes)"
                     data-content="Loading..." data-html="true" data-container="body"
                     data-id="${bug.id}" data-trigger="click" class="bug-summary">
                    ${escapeHTML(bug.summary)}
                  </a>
                </td>
                <td class="hidden-xs hidden-sm">${escapeHTML(bug.component)}</td>
                <td class="text-center hidden-xs" data-value="${bug.votes}">${bug.votes}
                (<a href="${voteLink}" target="_blank">Vote</a>)</td>
              </tr>
            `;
            elements += element;
        });

        var rendered = `${elements}`;

        return rendered;
    };

    // Fetch features
    bz.searchBugs({
        product: 'Firefox OS',
        resolution: '---',
        keywords: 'feature, foxfood',
    }).done(function(data) {
        var features = $('#features');
        features.html(render(data));
        $.bootstrapSortable();
        $('body').trigger('bugsloaded');
    });

    // Fetch defects
    bz.searchBugs({
        product: 'Firefox OS',
        resolution: '---',
        keywords: 'foxfood'
    }).done(function(data) {
        var defects = $('#defects');
        // Remove features from this list.
        data.bugs = data.bugs.filter(function(bug) {
            return bug.keywords.indexOf('feature') === -1;
        });
        defects.html(render(data));
        $.bootstrapSortable();
        $('body').trigger('bugsloaded');
    });
});
