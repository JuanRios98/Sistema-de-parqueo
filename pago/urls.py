from django.urls import path
from .views import PagoList, PagoDetail

urlpatterns = [
    path('pago/', PagoList.as_view(), name='Listado de Pagos'),
    path('pago/<int:pk>/', PagoDetail.as_view(), name='Detalle de Pago'),
]