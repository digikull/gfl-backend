from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response
from http.client import responses
from .models import Tournament
from .serializers import TournamentSerializer

class ListTournament(APIView):
    def get(self, request, format=None):
       
        tr = Tournament.objects.all()
        serializer = TournamentSerializer(tr, many = True)
     #   task = [Task.title for task in Task.objects.all()]
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({"msg":"create Api"})

         
