from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderDishForm, UpdateOrderForm
from .models import Order, OrderDish
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.utils.translation import ngettext_lazy

PENDING = 'В ожидании'


def index(request: WSGIRequest) -> HttpResponse:
    """
        Main page that contains table with all orders, with ability to search order by its status or table number
    """
    search_string = request.GET.get('q')
    orders = Order.objects
    if search_string:
        orders = orders.filter(
            Q(table_number__icontains=search_string) | Q(status__icontains=search_string)
        )
    orders = orders.all().order_by('-id')
    paginator = Paginator(orders, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'orders/index.html', {
        'page': page, 'paginator': paginator, 'orders': orders
    })


@login_required
def order_statistics(request: HttpRequest) -> HttpResponse:
    """
        Page with orders' total sum grouped by statuses
    """
    orders_by_status = Order.objects.values('status').annotate(
        total_sum=Sum('dishes__price'),
        total_count=Count('id', distinct=True)).order_by('status')
    paginator = Paginator(orders_by_status, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'orders/statistics.html', {
        'page': page, 'paginator': paginator
    })


@login_required
def add_order(request: HttpRequest) -> HttpResponse:
    """
        Add new order with dishes (allowed only for authenticated users)
    """
    custom_error_messages = {
        "too_few_forms": 'Необходимо указать хотя бы %(num)d блюдо'
    }
    formset_factory = inlineformset_factory(Order, OrderDish, form=OrderDishForm, fields=['name', 'price'],
                                            can_delete=False, min_num=1, validate_min=True,
                                            )
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        dishes_form = formset_factory(request.POST, error_messages=custom_error_messages)

        if order_form.is_valid() and dishes_form.is_valid():
            order = Order()
            order.table_number = order_form.cleaned_data['table_number']
            order.status = PENDING
            order.save()

            for dish_data in dishes_form.cleaned_data:
                if 'name' in dish_data and 'price' in dish_data:
                    dish = OrderDish()
                    dish.order = order
                    dish.name = dish_data['name']
                    dish.price = dish_data['price']
                    dish.save()

            return redirect('/')
        context = {"order_form": order_form, "items_formset": dishes_form}
    else:
        formset = formset_factory(instance=Order())
        context = {"items_formset": formset, 'order_form': OrderForm}

    return render(request, 'orders/add_order.html', context)


def order(request: HttpRequest, order_id: int) -> HttpResponse:
    """
        Page with information about individual order and ability to update order's status
    """
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            order.status = form.cleaned_data.get('status')
            order.save()
            return redirect('/')
    else:
        form = UpdateOrderForm(instance=order)

    return render(request, 'orders/order.html', {'order': order, 'form': form})


@login_required
def delete_order(request: HttpRequest, order_id: int) -> HttpResponse:
    """
        Delete existing order (allowed only for authenticated users)
    """
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'orders/delete_order.html', {'order': order})


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    """
        Custom page for 404 error
    """
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request: HttpRequest) -> HttpResponse:
    """
        Custom page for 500 error
    """
    return render(request, 'misc/500.html', status=500)
