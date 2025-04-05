from django.forms import ModelForm
from .models import Equipe, Joueur

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['nom', 'ville']

class JoueurForm(ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'poste', 'equipe']
