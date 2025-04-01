from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
