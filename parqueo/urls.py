from django.urls import path
from .views import ParqueoList, ParqueoDetail


urlpatterns = [
    path('parqueo/', ParqueoList.as_view(), name='parqueo_list'),
    path('parqueo/<int:pk>/', ParqueoDetail.as_view(), name='parqueo_detail'),
]