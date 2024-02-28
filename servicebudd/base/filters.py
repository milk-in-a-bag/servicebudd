import django_filters
from .models import ServiceProvider

class ServiceProviderFilter(django_filters.FilterSet):
    class Meta:
        model = ServiceProvider
        fields = ['location', 'starting_price']