from .views import ListClient

from django.urls import path

urlpatterns = [
    path('clients/', ListClient.as_view(), name='lista-clientes')
]