
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.



@api_view(['GET'])
def get_all_players(request):
    players = Player.objects.all()
    player_list= []

    for player in players:
        result = {
            "pk":player.pk,
            "name":player.name,
            "role":player.role,
            "city":player.city,
            "image":player.image

        }
        player_list.append(result)
        serializer = PlayerSerializer(player_list, many=True)
    return Response(serializer.data)
  

@api_view(['GET'])
def get_player(request,pk):
    try:
        player = player.objects.get(pk=pk)
    except:
        return Response({"message":"player does not exist"},status=404)

    result = {
        "pk":player.pk,
        "name":player.name,
        "role":player.role,
        "city":player.city,
        "image":player.image
    }
    serializer = PlayerSerializer(result, many=True)
    return Response(serializer.data)
   

@api_view(['POST'])
def create_player(request):
    name = request.data['name']
    role=request.data['role']
    city=request.data['city']
    image=request.data['image']
    player = Player.objects.create(name=name , role=role ,city=city ,image=image)
    player.save()
    return Response({"message":"player inserted successfully"})

@api_view(['PUT'])
def update_player(request,pk):
    name = request.data['name']
    role = request.data['role']

    player = Player.objects.get(pk=pk)
    player.name = name
    player.role = role
    player.city=city
    player.image=image
    player.save()
    return Response({"message":"player updated successfully"})

@api_view(['DELETE'])
def delete_player(request,pk):
    player = Player.objects.filter(pk=pk).delete()
    return Response({"message":"player deleted successfully"})