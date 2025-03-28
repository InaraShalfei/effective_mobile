from django import forms
from .models import Order, OrderDish


class OrderForm(forms.ModelForm):
    table_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1,
        step_size=1,
        label='номер стола',
    )

    class Meta:
        model = Order
        fields = ['table_number']


class OrderDishForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='название блюда',
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0,
        step_size=1,
        label='стоимость блюда',
    )

    class Meta:
        model = OrderDish
        fields = ['order', 'name', 'price']


class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

    status = forms.ChoiceField(
        choices=Order.STATUSES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'choice-select'}),
        label=''
    )
