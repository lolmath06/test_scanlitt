from rest_framework import serializers
from .models import Equipe, Joueur, Match

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'

class JoueurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joueur
        fields = '__all__'

    def validate(self, data):
        equipe = data.get('equipe')
        if equipe.joueurs.count() >= 11:
            raise serializers.ValidationError("Cette équipe a déjà 11 joueurs.")
        return data

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
