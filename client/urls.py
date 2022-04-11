from .views import ListClient, DetailClient

from django.urls import path

urlpatterns = [
    path('clients/', ListClient.as_view(), name='lista-clientes'),
    path('clients/<pk>', DetailClient.as_view(), name='detail-clientes')
]
