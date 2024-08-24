from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViagemViewSet, DestinoViewSet

router = DefaultRouter()
router.register(r'viagens', ViagemViewSet)
router.register(r'destinos', DestinoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
