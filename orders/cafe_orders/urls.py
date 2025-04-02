from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.order_statistics, name='statistics'),
    path('add/', views.add_order, name='add_order'),
    path('order/<int:order_id>/', views.order,
         name='order'),
    path('order/<int:order_id>/delete', views.delete_order,
         name='delete_order')
]
