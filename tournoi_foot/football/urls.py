from django.urls import path, include
from rest_framework import routers
from .views import EquipeViewSet, create_equipe

router = routers.DefaultRouter()
router.register(r'equipes', EquipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('equipe/new/', create_equipe, name='create_equipe'),
]
