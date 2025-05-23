# products/filters.py
import django_filters
from django.db.models import Q
from .models import Product, Tag, Category

class ProductFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), field_name='tags__id')
    
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    condition = django_filters.CharFilter(field_name='condition')
    
    free = django_filters.BooleanFilter(method='filter_free_products')
    offers = django_filters.BooleanFilter(method='filter_active_offers')

    class Meta:
        model = Product
        fields = []

    def filter_free_products(self, queryset, name, value):
        if value:
            return queryset.filter(price=0)
        return queryset

    def filter_active_offers(self, queryset, name, value):
        if value:
            return queryset.filter(offer__active=True)
        return queryset
