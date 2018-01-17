import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WorldWideEnzyme.settings')
import django
django.setup()
import xml.etree.ElementTree as ET
from app.models import *
import re

EC = r'EC \d\.\d{1,2}\.\d{1,2}\.\w{1,3} '
for ec in Enzyme.objects.all():
    his = ec.history
    print(his)
    try:
        res = re.sub(r'\(.*\)','',his[re.match(EC,his).end():])
    except:
        continue
    print(res)
    for a in res.split(','):
        try:
            year = re.search(r'\d{4}',a).group()
            TimelineEvent.objects.create(enzyme=ec,year=year,content=a)
        except:
            pass

