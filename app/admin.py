from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(Enzyme)
admin.site.register(Prosite)
admin.site.register(Swissprot)
admin.site.register(Synonym)
admin.site.register(Article)
admin.site.register(Cofactor)

