from django import template
import re

register = template.Library()

@register.filter(name='ec')
def ec(value):
    url_ec = '/enzymes/'
    return re.sub(r'EC (\d\.\d{1,2}\.\d{1,2}\.\w{1,3})',r'<a href="{0}\1">EC \1</a>'.format(url_ec),value)

@register.filter(name='search_include')
def search_include(result):
    t = result.content_type().split('.')
    return 'search/includes/{}/{}.html'.format(t[0],t[1])
