from django.urls import path
from basic.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', Serializejson.as_view(), name = 'serialize_url'), #весь json формат на странице
    path('table/', Table.as_view(), name = 'table_url'),# главная таблица
    path('table/create/', CreateCampony.as_view(), name='campony_create_url'),#добавляем новую компанию
    path('items/', manage_items, name="items"),#отображаем Redis проверка данных
]

urlpatterns = format_suffix_patterns(urlpatterns)