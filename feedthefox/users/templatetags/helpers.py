import jinja2
from allauth.socialaccount.templatetags.socialaccount import (get_providers as
                                                              social_get_providers)
from allauth.socialaccount import providers
from allauth.utils import get_request_param
from django_jinja import library


@library.global_function
def get_providers():
    return social_get_providers()


@library.global_function
@jinja2.contextfunction
def provider_login_url(context, provider_id, **params):
    """
    {{ provider_login_url("persona", next="/some/url")}}
    {{ provider_login_url("github", next="/some/other/url")}}
    """
    request = context['request']
    provider = providers.registry.by_id(provider_id)
    auth_params = params.get('auth_params', None)
    scope = params.get('scope', None)
    process = params.get('process', None)
    if scope is '':
        del params['scope']
    if auth_params is '':
        del params['auth_params']
    if 'next' not in params:
        next = get_request_param(request, 'next')
        if next:
            params['next'] = next
        elif process == 'redirect':
            params['next'] = request.get_full_path()
    else:
        if not params['next']:
            del params['next']
    return jinja2.Markup(provider.get_login_url(request, **params))


@library.global_function
@jinja2.contextfunction
def providers_media_js(context):
    """
    {{ providers_media_js() }}
    """
    return jinja2.Markup(u'\n'.join([provider.media_js(context['request'])
                                     for provider in providers.registry.get_list()]))
