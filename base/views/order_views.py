from base.models.order import OrderItem
from django.shortcuts import render, redirect
from base.forms.order_form import OrderForm
from base.addcart import Cart
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def bulling_information_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    orderItem=order,
                    products=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return redirect('pos_view')
    else:
        form = OrderForm()
    return render(request, 'pos/bulling_information.html', {'form': form, 'cart': cart})


class OrderItemView(ListView):
    template_name = 'pos/order_list.html'
    model = OrderItem
    context_object_name = 'order'
    paginate_by = 15

@login_required(login_url='login')
def search_orders(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        search_button = request.GET.get('submit')
        if query is not None:
            condition =  Q(price__icontains=query) | Q(quantity__icontains=query)  
            final_result = OrderItem.objects.filter(condition).distinct()
            context = {
                'final_result': final_result,
                'search_button': search_button
            }
            return render(request, 'orders/search_orders.html', context)
        else:
            return render(request, 'orders/order_list_complonent.html')
    else:
        return render(request, 'orders/order_list_complonent.html')
