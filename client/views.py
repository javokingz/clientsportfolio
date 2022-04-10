from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Client
from rest_framework.views import APIView
from rest_framwork.respose import Response



class ClientListView(ListView):
    """Clients view."""
    template_name = 'index.html'
    queryset = Client.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        return context

class ListClient(APIView):
    
    def get(self, request):
        clients = Client.objects.all()
        return Response(clients)



