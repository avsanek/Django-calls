from django_filters import rest_framework as filters
import django_filters
from django.utils.translation import gettext_lazy as _


from django.forms import Textarea
from .models import Book






class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class BookFilter(filters.FilterSet):
    # asd = CharFilterInFilter(field_name='Number2N')
    # qwe = CharFilterInFilter(field_name='Number1M')
    #
    # TimeStartJ = filters.RangeFilter()
    # Tel1B = filters.CharFilter(field_name='Tel1B__Tel2C')
    # name = filters.CharFilter(field_name='Typ_zvonkaD', lookup_expr='gt')
    TimeStartJ = filters.CharFilter(field_name='TimeStartJ', lookup_expr='icontains') # потестить дату, закачать фул базу
    Tel1B = filters.CharFilter(field_name='Tel1B', lookup_expr='icontains')
    Tel2C = filters.CharFilter(field_name='Tel2C', lookup_expr='icontains')
    KtoE = filters.CharFilter(field_name='KtoE', lookup_expr='icontains')



    class Meta:
        model = Book
        fields = ['Typ_zvonkaD']

    def __init__(self, *args, **kwargs):
        super(BookFilter, self).__init__(*args, **kwargs)
        self.filters['TimeStartJ'].label = 'Дата'
        self.filters['KtoE'].label='Кто звонилE'
        self.filters['Tel1B'].label='Телефон1B'
        self.filters['Tel2C'].label='Телефон2C'
        self.filters['Typ_zvonkaD'].label='Тип звонкаD'


# class BookFilter(django_filters.FilterSet):
#     class Meta:
#         model = Book
#         fields = ['KtoE','Tel1B', 'Tel2C','Typ_zvonkaD']
#
#
#
#     def __init__(self, *args, **kwargs):
#         super(BookFilter, self).__init__(*args, **kwargs)
#         self.filters['KtoE'].label='Кто звонилE'
#         self.filters['Tel1B'].label='Телефон1B'
#         self.filters['Tel2C'].label='Телефон2C'
#         self.filters['Typ_zvonkaD'].label='Тип звонкаD'
#
        

