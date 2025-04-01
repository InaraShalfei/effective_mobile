from rest_framework import serializers
from djoser.serializers import UserSerializer

from cafe_orders.models import CustomUser, OrderDish, Order, STATUSES


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'id', 'username', 'first_name', 'last_name')


class OrderDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDish
        fields = ('name', 'price')


class OrderSerializer(serializers.ModelSerializer):
    dishes = OrderDishSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    status = serializers.ChoiceField(choices=STATUSES)

    class Meta:
        model = Order
        fields = ('id', 'table_number', 'status', 'total_price', 'dishes')

    def get_total_price(self, obj):
        return sum([dish.price for dish in obj.dishes.all()])
