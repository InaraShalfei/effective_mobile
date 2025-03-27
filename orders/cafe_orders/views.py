from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, OrderDishForm
from .models import Order, OrderDish
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    orders = Order.objects.all().order_by('-id')
    paginator = Paginator(orders, settings.ITEMS_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'orders/index.html', {
        'page': page, 'paginator': paginator, 'orders': orders
    })


def add_order(request):
    formset_factory = inlineformset_factory(Order, OrderDish, form=OrderDishForm, fields=['name', 'price'],
                                            can_delete=False)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = Order()
            order.table_number = order_form.cleaned_data['table_number']
            order.status = 'Pending'
            order.save()
            dishes_form = formset_factory(request.POST)
            print(dishes_form.cleaned_data)

            return redirect('/orders')
        context = {"order_form": order_form}
    else:
        formset = formset_factory(instance=Order())
        context = {"items_formset": formset, 'order_form': OrderForm}

    return render(request, 'orders/add_order.html', context)


def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_form = OrderForm(instance=order)

    return render(request, 'orders/order.html', {'order': order, 'form': order_form})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
    return redirect('/orders/order/')


def page_not_found(request, exception):
    return render(request, 'misc/404.html', {'path': request.path}, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'misc/403.html', status=403)
