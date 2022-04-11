from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Client
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClientSerializer



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
        client_json = ClientSerializer(clients, many=True)
        return Response(client_json.data)
    
    def post(self, request):
        client_json = ClientSerializer(data=request.data)
        if client_json.is_valid():
            client_json.save()
            return Response(client_json.data, status=201)
        return Response(client_json.error, status=400)
    
class DetailClient(APIView):

    def get(self, request, pk):
        try:

            client = Client.objects.get(pk=pk)
            client_json = ClientSerializer(client)
            return Response(client_json.data)
        except Client.DoesNotExist:
            raise Http404
    
    def get_object(self, pk):
        try:
           return Client.objects.get(pk=pk)
           
        except Client.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        
       client = self.get_object(pk)
       client_json = ClientSerializer(client, data=request.data)
       if client_json.is_valid():
           client_json.save()
           return Response(client_json.data)
       return Response(client_json.errors, status= 400)
    

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=204)








