from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.db.models import Sum, Case, When, IntegerField, F

from .models import Equipe, Joueur, Match
from .serializers import EquipeSerializer, JoueurSerializer, MatchSerializer
from .forms import JoueurForm

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class ClassementView(APIView):
    def get(self, request):
        return classement(request)

class JoueurFormView(APIView):
    def get(self, request):
        return create_joueur(request)
    def post(self, request):
        return create_joueur(request)

@api_view(['GET'])
def classement(request):
    equipes = Equipe.objects.annotate(
        points=Sum(
            Case(
                When(matchs_dom__buts_equipe1__gt=F('matchs_dom__buts_equipe2'), then=3),
                When(matchs_dom__buts_equipe1=F('matchs_dom__buts_equipe2'), then=1),
                default=0,
                output_field=IntegerField()
            ) +
            Case(
                When(matchs_ext__buts_equipe2__gt=F('matchs_ext__buts_equipe1'), then=3),
                When(matchs_ext__buts_equipe2=F('matchs_ext__buts_equipe1'), then=1),
                default=0,
                output_field=IntegerField()
            )
        ),
        buts_marques=Sum('matchs_dom__buts_equipe1') + Sum('matchs_ext__buts_equipe2'),
        buts_recus=Sum('matchs_dom__buts_equipe2') + Sum('matchs_ext__buts_equipe1'),
    ).order_by('-points', '-buts_marques')

    data = [
        {
            'equipe': equipe.nom,
            'points': equipe.points or 0,
            'buts_marques': equipe.buts_marques or 0,
            'buts_recus': equipe.buts_recus or 0
        }
        for equipe in equipes
    ]

    return Response(data)

def create_joueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_joueur')
    else:
        form = JoueurForm()

    return render(request, 'football/create_joueur.html', {'form': form})
