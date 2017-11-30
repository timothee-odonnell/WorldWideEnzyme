from django.db import models
from django.urls import reverse

class Enzyme(models.Model):
    STATUS = {('D','Deleted'),('T','Transferred'),('E','Existed')}
    label = models.CharField(max_length=20,primary_key=True)
    accepted_name = models.CharField(null=True,max_length=256)
    systematic_name = models.CharField(null=True,max_length=256)
    status = models.CharField(max_length=1,choices=STATUS,default='E')
    note = models.TextField(null=True)
    activity = models.TextField(null=True)
    comment = models.TextField(null = True)
    disease = models.TextField(null = True)
    history = models.TextField(null = True)

    def __str__(self):
        return 'Enzyme : '+self.label

    def check_or_add(self,name):
        assert name
        if (self.accepted_name != name) and (self.systematic_name != name):
            self.synonym_set.get_or_create(label=name)

    def get_absolute_url(self):
        return reverse('enzyme_page',args=[self.label])

class Prosite(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.enzyme.label + ' ' + self.label

class Swissprot(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.CharField(max_length=10)
    name = models.CharField(max_length=16)

    def __atr__(self):
        return self.enzyme + ' ' + self.label

class Cofactor(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    cofactor = models.CharField(max_length=64)

    def __str__(self):
        return self.enzyme.label + ' ' + self.cofactor

class Synonym(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.TextField()

    def __str__(self):
        return "EC " + self.enzyme.label + " : " + self.label

class Article(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    title = models.TextField()
    year = models.IntegerField(null=True)
    volume = models.CharField(null=True,max_length=16)
    first_page = models.CharField(null=True,max_length=16)
    last_page = models.CharField(null=True,max_length=16)
    editorial = models.CharField(null=True,max_length=128)
    edition = models.CharField(null=True,max_length=128)
    editor = models.CharField(null=True,max_length=128)
    pubmed = models.IntegerField(null=True)
    medline = models.IntegerField(null=True)

    def __str__(self):
        return self.title
