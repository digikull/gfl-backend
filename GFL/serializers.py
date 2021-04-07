
from rest_framework import serializers
from .models import Tournament

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'tournament_name', 'tournament_type','tournament_class','tournament_total_team','tournament_template','tournament_detials','lat','lon']