from django.urls import path, include
from rest_framework import routers
from .views import EquipeViewSet, JoueurViewSet, MatchViewSet, create_joueur, classement, ClassementView, JoueurFormView

router = routers.DefaultRouter()
router.register(r'equipes', EquipeViewSet)
router.register(r'joueurs', JoueurViewSet)
router.register(r'matchs', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('joueur/new/', create_joueur, name='create_joueur'),
    path('classement/', classement, name='classement'),
    path('classement/', ClassementView.as_view(), name='classement'),
    path('joueur/new/', JoueurFormView.as_view(), name='create_joueur'),
]
