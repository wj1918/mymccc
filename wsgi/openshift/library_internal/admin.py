from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.db.models import get_models, get_app

for model in get_models(get_app('library_internal')):
    admin.site.register(model)

