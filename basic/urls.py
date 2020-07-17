from django.urls import path
from basic.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', Serializejson.as_view(), name = 'serialize_url'),
    path('table/', Table.as_view(), name = 'table_url'),
    path('table/create/', CreateCampony.as_view(), name='campony_create_url')
]

urlpatterns = format_suffix_patterns(urlpatterns)