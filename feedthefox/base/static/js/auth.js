(function() {
    var allauth = window.allauth = window.allauth || {};

    function startWatching() {
        navigator.id.watch({
            onlogin: function(assertion) {
                // TODO: next url handling
                document.getElementById("_persona_assertion").value = assertion;
                document.getElementById("_persona_login").submit();
            },
            onlogout: function() {
                // TODO
            }
        })
    };

    allauth.persona = {
        login: function(nextUrl, process) {
            document.getElementById("_persona_next_url").value = nextUrl || '';
            document.getElementById("_persona_process").value = process;
            startWatching();
            navigator.id.request({});
        }
    }
})();
