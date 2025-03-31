from django.db.models import Q

from .models import Order


def order_search(el):
    return Order.objects.filter(
            Q(table_number__icontains=el) | Q(status__icontains=el)
        )[:5]
