import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WorldWideEnzyme.settings')
import django
django.setup()
import xml.etree.ElementTree as ET
from app.models import *

def parse_db_enzyme():
    f = open('intenz.txt')
    for line in f:
        obj = ET.fromstring('<H>'+line+'</H>')
        ID = obj.find('ec').text.split()[-1]
        try:
            a_name = obj.find('accepted_name').text
            s_name = obj.find('systematic_name').text
            enz = Enzyme.objects.create(label=ID,accepted_name=a_name,systematic_name=s_name,history=history)
        except Exception as e:
            print(e)
            enz = Enzyme.objects.create(label=ID,is_deleted=True,history=history)
        try:
            history = obj.find('history').text
            enz.history = history
        except:
            pass
        enz.save()
        try:
            for s in obj.findall('synonym'):
                Synonym.objects.create(enzyme=enz,label=s.text)
        except:
            pass
        print(enz)


if __name__ == '__main__':
    parse_db_enzyme()
