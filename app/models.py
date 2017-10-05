from django.db import models

class Enzyme(models.Model):
    label = models.CharField(max_length=20)
    accepted_name = models.CharField(null=True,max_length=256)
    systematic_name = models.CharField(null=True,max_length=256)
    is_deleted = models.BooleanField(default=False)
    activity = models.TextField(null=True)
    comment = models.TextField(null = True)
    disease = models.TextField(null = True)
    history = models.TextField(null = True)

    def __str__(self):
        return 'Enzyme : '+self.label

class Prosite(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.enzyme + ' ' + self.label

class Swissprot(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.CharField(max_length=10)
    name = models.CharField(max_length=16)

    def __atr__(self):
        return self.enzyme + ' ' + self.label

class Cofactor(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    cofactor = models.CharField(max_length=10)

class Synonym(models.Model):
    enzyme = models.ForeignKey(Enzyme)
    label = models.CharField(max_length=256)

    def __str__(self):
        return "EC " + self.enzyme.label + " : " + label
