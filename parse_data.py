import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WorldWideEnzyme.settings')
import django
django.setup()
import xml.etree.ElementTree as ET
from app.models import *
import re

# Editorial place is an attrib of <editorial>.
# Since the place of Academic Press is always New York, I didn't write the code to extract place's information
def parse_intenz():
    f = open('intenz_modified.txt')
    for line in f:
        obj = ET.fromstring('<H>'+line+'</H>')
        ID = obj.find('ec').text.split()[-1]
        try:
            a_name = obj.find('accepted_name').text
            s_name = obj.find('systematic_name').text
            enz = Enzyme.objects.create(label=ID,accepted_name=a_name,systematic_name=s_name)
        except Exception as e:
            tmp = obj.find('deleted')
            status='D'
            if not tmp:
                tmp = obj.find('transferred')
                status='T'
            try:
                note = tmp.find('note').text
            except:
                note = ''
            enz = Enzyme.objects.create(label=ID,status=status,note = note)
        try:
            history = obj.find('history').text
            enz.history = history
        except:
            pass
        try:
            enz.comment = '\r'.join([c.text for c in obj.findall('comment')])
        except:
            pass
        enz.save()
        try:
            for s in obj.findall('synonym'):
                Synonym.objects.create(enzyme=enz,label=s.text)
        except:
            pass
        try:
            for a in obj.findall('article'):
                data = {'enzyme':enz}
                for tmp in a.getchildren()[1:]:
                    data[tmp.tag] = tmp.text
                Article.objects.create(**data)                
        except Exception as e:
            print(e)
            print(enz)
            break

def parse_db_enzyme():
    pattern = r"<EC>EC (?P<label>.*)</EC>\t<S_NAME>(?P<accepted_name>.*)\.</S_NAME>\t<O_NAME>(?P<other_name>.*)</O_NAME>\t<ACTIVITY>(?P<activity>.*)</ACTIVITY>\t<COFACTORS>(?P<cofactors>.*)</COFACTORS>\t<COMMENTS>(?P<comment>.*)</COMMENTS>\t<DISEASE>(?P<disease>.*)</DISEASE>\t<PROSITE>(?P<prosites>.*)</PROSITE>\t<SWISSPROT>(?P<swissprots>.*)</SWISSPROT>"
    f = open('db_enzyme.txt')
    for line in f:
        obj = re.match(pattern,line[:-1])
        dic = obj.groupdict()
        try:
            ec = Enzyme.objects.get(label=dic['label'])
        except:
            Enzyme.objects.create(label=dic['label'],status='D')
            continue
        if not ec.status == 'E':
            continue
        ec.activity = dic['activity']
        ec.save()
        if dic['accepted_name']:
            ec.check_or_add(dic['accepted_name'])
        if dic['other_name']:
            ec.check_or_add(dic['other_name'])
        for p in dic['prosites'].split(';'):
            if p:
                Prosite.objects.create(enzyme=ec,label=p)
        for s in dic['swissprots'].split(';'):
            if s:
                lst = s.split(',')
                Swissprot.objects.create(enzyme=ec,label=lst[0],name=lst[1])

        for c in dic['cofactors'][:-1].replace(' or',';').split('; '):
            if c:
                Cofactor.objects.create(enzyme=ec,cofactor=c.title())

def modify_intenz():
    """
    The function inserts <article></article> tag into intenz.txt,
    then writes the result in the new file intenz_modified.txt .
    """
    f = open('intenz.txt','r')
    g = open('intenz_modified.txt','w')

    for line in f:
        arts = [m.start() for m in re.finditer('<authors>',line)]
        if arts == []:
            print(line[:-1],file=g)
            continue
        try:
            lst_ind = line.find('<history>')
        except:
            lst_ind = -1
        new_str = line[:(arts[0]-1)]
        for i in range(len(arts)):
            if i == 0:
                new_str += '<article>'
                if len(arts) > 1:
                    new_str += line[arts[0]:(arts[1]-1)]
                else:
                    new_str += line[arts[0]:(lst_ind-1)]
            elif i == len(arts)-1:
                new_str += '</article><article>'
                new_str += line[arts[-1]:(lst_ind-1)]
            else:
                new_str += '</article><article>'
                new_str += line[arts[i]:(arts[i+1]-1)]
        new_str += '</article>'
        new_str += line[lst_ind:]
        print(new_str[:-1],file=g)

if __name__ == '__main__':
    parse_intenz()
    parse_db_enzyme()
    #modify_intenz()
