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
    status = serializers.ChoiceField(
        choices=STATUSES,
        error_messages={
            'invalid_choice': f'Invalid status choice. Please choose from {[value[0] for value in STATUSES]}'}
    )

    class Meta:
        model = Order
        fields = ('id', 'table_number', 'status', 'total_price', 'dishes')

    def get_total_price(self, obj):
        return sum([dish.price for dish in obj.dishes.all()])

    def create(self, validated_data):
        dishes = validated_data.pop('dishes')
        order = Order.objects.create(**validated_data)

        for dish in dishes:
            OrderDish.objects.create(**dish, order=order)

        return order

    def update(self, instance, validated_data):
        instance.table_number = validated_data.get('table_number', instance.table_number)
        instance.status = validated_data.get('status', instance.status)
        instance.total_price = validated_data.get('total_price', instance.total_price)

        instance.save()

        dishes_data = validated_data.pop('dishes', None)
        if dishes_data is not None:
            for dish_data in dishes_data:
                OrderDish.objects.create(order=instance, **dish_data)

        return instance
