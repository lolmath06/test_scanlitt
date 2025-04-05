from django.test import TestCase
from rest_framework.test import APIClient
from .models import Equipe, Joueur

class EquipeJoueurTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.equipe = Equipe.objects.create(nom="OGC Nice", ville="Nice")

    def test_creation_equipe(self):
        response = self.client.post('/api/equipes/', {'nom': 'PSG', 'ville': 'Paris'})
        self.assertEqual(response.status_code, 201)

    def test_limite_joueurs_equipe(self):
        for i in range(11):
            Joueur.objects.create(nom=f'Joueur{i}', poste='Gardien', equipe=self.equipe)
        response = self.client.post('/api/joueurs/', {'nom': 'ExtraJoueur', 'poste': 'Gardien', 'equipe': self.equipe.id})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Cette équipe a déjà 11 joueurs.', str(response.data))
