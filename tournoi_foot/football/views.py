from rest_framework import viewsets
from .models import Equipe
from .serializers import EquipeSerializer
from django.shortcuts import render, redirect
from .forms import EquipeForm

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer

def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_equipe')  # Tu peux ajuster après
    else:
        form = EquipeForm()
    return render(request, 'football/create_equipe.html', {'form': form})
