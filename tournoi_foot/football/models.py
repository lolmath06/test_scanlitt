from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
