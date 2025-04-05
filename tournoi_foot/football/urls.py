from django.urls import path, include
from rest_framework import routers
from .views import EquipeViewSet, JoueurViewSet

router = routers.DefaultRouter()
router.register(r'equipes', EquipeViewSet)
router.register(r'joueurs', JoueurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
