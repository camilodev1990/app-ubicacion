from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UbicacionViewSet

router = DefaultRouter()
router.register(r"ubicaciones", UbicacionViewSet, basename="ubicacion")

urlpatterns = [
    path("", include(router.urls)),
]
