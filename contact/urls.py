from . import views

from django.urls import path, include

urlpatterns = [
    path('contact/', views.Contact, name="contact"),
    
]