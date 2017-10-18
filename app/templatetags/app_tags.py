from django import template
from django.urls import reverse
import re

register = template.Library()

@register.filter(name='ec')
def ec(value):
    url_ec = str(reverse('enzyme_page',args=['']))
    return re.sub(r'EC (\d\.\d{1,2}\.\d{1,2}\.\w{1,3})',r'<a href="{0}\1">EC \1</a>'.format(url_ec),value)
