from . import views
from django.urls import path

urlpatterns = [
    
    path('export/xls/', views.export_client_xls, name='export_client_xls'),
]