import django_filters 
from .models import Pictures

class PictureFilter(django_filters.FilterSet):

    class Meta:
        model = Pictures
        fields = {
            'created_at':['icontains','lte','gte'],
            'updated_at':['icontains','lte','gte'],
            'title':['icontains'],
        }