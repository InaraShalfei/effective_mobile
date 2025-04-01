from rest_framework import viewsets

from api.serializers import OrderSerializer
from cafe_orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
