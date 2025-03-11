from django.urls import path
from .views import VehiculoList, VehiculoDetail

urlpatterns = [
    path('vehiculo/', VehiculoList.as_view()),
    path('vehiculo/<int:pk>/', VehiculoDetail.as_view()),
]