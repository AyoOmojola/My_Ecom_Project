from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from app_order.models import Cart,Order
from django.contrib import messages
from app_shop.models import Product
# Create your views here.

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, 'This item quantity was updated')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, 'This item is added to your cart')
            return redirect('app_shop:home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, 'This item is added to your cart')
        return redirect('app_shop:home')


@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'app_order/cart.html', context={'carts':carts,'orders':orders})
    else:
        messages.warning(request, 'You dont have any item in your cart')
        return redirect('app_shop:home')


