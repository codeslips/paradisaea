from django_filters import FilterSet
from .models import ListModel

class Filter(FilterSet):
    class Meta:
        model = ListModel
        fields = {
            "sender": ['exact', 'iexact',  'contains', 'icontains', 'isnull', 'in', 'range'],          
            "receiver": ['exact', 'iexact',  'contains', 'icontains', 'isnull', 'in', 'range'],
            "read": ['exact', 'iexact',  'contains', 'icontains', 'isnull', 'in', 'range'], 
            "detail": ['exact', 'iexact',  'contains', 'icontains', 'isnull', 'in', 'range'],           
            "create_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range'],
            "update_time": ['year', 'month', 'day', 'week_day', 'gt', 'gte', 'lt', 'lte', 'range']
        }
