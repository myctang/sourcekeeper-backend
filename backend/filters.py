import django_filters
from backend.models import Source

class SourceFilter(django_filters.FilterSet):
    sources = django_filters.CharFilter(
        name='tags',
        lookup_expr='contains',
    )

    class Meta:
        model = Source
        fields = ('tags', 'color', 'author', 'language',)