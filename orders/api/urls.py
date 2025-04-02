from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from djoser import views as djoser_views

from api.views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)

user_registration = djoser_views.UserViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    re_path(r"^auth/jwt/create/?", jwt_views.TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^auth/users/", user_registration, name="user-create"),
    path('', include(router.urls))
]
