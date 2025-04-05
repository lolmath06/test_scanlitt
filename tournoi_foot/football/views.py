from rest_framework import viewsets
from .models import Equipe, Joueur
from .serializers import EquipeSerializer, JoueurSerializer
from django.shortcuts import render, redirect
from .forms import JoueurForm

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

class JoueurViewSet(viewsets.ModelViewSet):
    queryset = Joueur.objects.all()
    serializer_class = JoueurSerializer

def create_joueur(request):
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_joueur')
    else:
        form = JoueurForm()
    return render(request, 'football/create_joueur.html', {'form': form})