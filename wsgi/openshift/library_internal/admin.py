from django.contrib import admin

# Register your models here.

from library_internal.models import CbDb
from library_internal.models import EbDb

class CbDbAdmin(admin.ModelAdmin):
    list_display= ('title', 'author','classnumber')
    list_filter = ['classnumber']
    search_fields= ['title','author','classnumber']

admin.site.register(CbDb,CbDbAdmin)
admin.site.register(EbDb)

