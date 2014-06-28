from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.db.models import get_models, get_app
import library_internal.models

a="class {0}Admin(admin.ModelAdmin):\n\
    list_display = {0}._meta.get_all_field_names()\n\
\n\
admin.site.register({0}, {0}Admin)\n"

for model in get_models(get_app('library_internal')):
    print a.format(model.__name__)




