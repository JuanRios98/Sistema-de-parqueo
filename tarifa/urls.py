from django.urls import path
from .views import TarifaList, TarifaDetail

urlpatterns = [

    path ('tarifa/', TarifaList.as_view(), name='tarifa_list'),
    path ('tarifa/<int:pk>/', TarifaDetail.as_view(), name='tarifa_detail'),

]
