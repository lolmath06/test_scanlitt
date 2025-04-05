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
    equipe = models.ForeignKey(Equipe, related_name='joueurs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.poste})"

    def clean(self):
        if self.equipe.joueurs.count() >= 11:
            raise ValidationError("Cette équipe a déjà atteint la limite maximale de 11 joueurs.")

class Match(models.Model):
    equipe1 = models.ForeignKey(Equipe, related_name='matchs_dom', on_delete=models.CASCADE)
    equipe2 = models.ForeignKey(Equipe, related_name='matchs_ext', on_delete=models.CASCADE)
    buts_equipe1 = models.IntegerField()
    buts_equipe2 = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipe1} vs {self.equipe2}"
