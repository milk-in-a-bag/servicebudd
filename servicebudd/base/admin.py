from django.contrib import admin
from .models import ServiceProvider, Filter, Review

# Register your models here.

admin.site.register(ServiceProvider)
admin.site.register(Filter)
admin.site.register(Review)