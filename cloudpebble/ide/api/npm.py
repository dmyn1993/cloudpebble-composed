import urllib
import requests

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe
from django.http import Http404

from utils.td_helper import send_td_event
from utils.jsonview import json_view
from utils.filter_dict import filter_dict

__author__ = 'katharine'

PACKAGE_SPEC = {
    'version': True,
    'name': True,
    'description': True,
    'keywords': True,
    'author': True,
    '_id': 'name'
}


@login_required
@require_safe
@json_view
def npm_search(request):
    try:
        query = request.GET['q']
    except KeyError:
        return {'packages': []}
    search = requests.get('https://registry.npmjs.com/-/v1/search', {'text': query, 'size': 20}).json()

    data = {'packages': []}

    for p in search['objects']:
        data['packages'].append({
            'name': p['package']['name'],
            'version': p['package']['version'],
            'description': p['package']['description'] if 'description' in p['package'] else '',
            'keywords': p['package']['keywords'] if 'keywords' in p['package'] else [],
            'author': p['package']['author']['name'] if 'author' in p['package'] else ''
        })

    send_td_event('cloudpebble_package_search', data={
        'data': {
            'query': query
        }
    }, request=request)
    return data


@login_required
@require_safe
@json_view
def npm_info(request):
    query = request.GET['q']

    try:
        package = requests.get('http://node-modules.com/package/%s.json' % urllib.quote(query)).json()
    except ValueError:
        raise Http404("Package not found")

    data = {
        'package': filter_dict(package, PACKAGE_SPEC)
    }
    send_td_event('cloudpebble_package_get_info', data={
        'data': {
            'query': query
        }
    }, request=request)
    return data
