from django.db import models
from django.contrib.auth.models import AbstractUser

STATUSES = [
    ('В ожидании', 'В ожидании'),
    ('Готово', 'Готово'),
    ('Оплачено', 'Оплачено')
]


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        ordering = ('first_name', 'last_name',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_full_name()


class Order(models.Model):
    table_number = models.PositiveIntegerField(verbose_name='номер стола')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус заказа')
    total_price = models.IntegerField(default=0, verbose_name='сумма заказа')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property
    def order_total_price(self):
        self.total_price = sum([dish.price for dish in self.dishes.all()])
        return self.total_price

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number} - Статус: {self.status}"


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='dishes', verbose_name='заказ')
    name = models.CharField(max_length=150, verbose_name='название блюда')
    price = models.IntegerField(default=0, verbose_name='стоимость блюда')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
