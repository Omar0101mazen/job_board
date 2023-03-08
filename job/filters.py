import django_filters
from .models import job
class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = ['category','description']
        # exclude =  ('slug','owner','img','published_at','salary','Vacancy')
        