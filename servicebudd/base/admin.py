from django.contrib import admin
from .models import ServiceProvider
from .models import Filter

# Register your models here.

admin.site.register(ServiceProvider)
admin.site.register(Filter)