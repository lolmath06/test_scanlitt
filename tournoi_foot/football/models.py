from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Joueur(models.Model):
    POSTES = [
        ('Gardien', 'Gardien'),
        ('Défenseur', 'Défenseur'),
        ('Milieu', 'Milieu'),
        ('Attaquant', 'Attaquant'),
    ]

    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=20, choices=POSTES)

    def __str__(self):
        return f"{self.nom} ({self.poste})"
