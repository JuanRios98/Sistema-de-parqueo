from django.urls import path
from .views import CeldaList, CeldaDetail

urlpatterns = [
    path('celda/', CeldaList.as_view(), name='Listado de Celdas'),
    path('celda/<int:pk>/', CeldaDetail.as_view(), name='Detalle de Celda'),
]

