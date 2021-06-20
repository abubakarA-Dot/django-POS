from django.http import request
from base.forms.invoice_form import InvoiceForm, OrderItemForm
from decimal import Decimal
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from base.models.Invoice import Event
from django.core.checks import messages
from base.models import product
from base.models.product import Product
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from base.models.Invoice import Invoice
from base.models.order import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse


def create_order(request):
    context = {
        'products': Product.objects.all(),
        'events': Event.objects.all()
    }
    return render(request, 'orders/add_order.html', context)


def get_product(request):
    product_id = request.GET.get('product')
    # Getting the data of that specific Product
    product = Product.objects.get(id=product_id)
    data = {
        'rate': product.Price,
    }
    return JsonResponse(data)


def ajax_order_create(request):
    if request.method == 'POST':
        # Getting the data from form inputs from ajax.
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        sub_total = request.POST.get('sub_total')
        # The String coming from ajax is e.g "["40", "42"]", converting this to "40", "42"
        products = product[1:-1]
        quantities = quantity[1:-1]
        sub_totals = sub_total[1:-1]

        # Converting string to array using python split() method
        products_list = products.split(',')
        quantities_list = quantities.split(',')
        sub_totals_list = sub_totals.split(',')
        # Slicing the double quotes (") from array indexes and converting them to decimals
        sub_totals_list = [x.strip(' "') for x in sub_totals_list]
        sub_totals_list = [Decimal(i) for i in sub_totals_list]
        # Slicing the double quotes (") from array indexes and converting them to int
        quantities_list = [x.strip(' "') for x in quantities_list]
        quantities_list = [int(i) for i in quantities_list]
        # product_list contains the id's of products/items selected in form
        products_list = [x.strip(' "') for x in products_list]
        products_list = [int(i) for i in products_list]
        # Creating the order object
        order = Order.objects.create(
            full_name='Abu Bakar',
            phn_number='03006890011',
            email='abubakar@gmail.com',
            address='Model Town Lahore'
        )
        for i in range(len(products_list)):
            OrderItem.objects.create(
                orderItem=order,
                products_id=products_list[i],
                price=sub_totals_list[i],
                quantity=quantities_list[i],
            )
    data = {'name': 'Faizan'}
    return JsonResponse(data)

# def add_order(request):
#     form = InvoiceForm()
#     if request.method == "POST":
#         form = InvoiceForm(request.POST or None)
#         if form.is_valid:
#             form.save()
#             #name = Product.objects.only('product_name').get(baseentity_ptr = request.POST.get('Product_id'))
#             sale = Product.objects.only('stock').get(baseentity_ptr = request.POST.get('Product_id'))
#             qty = int(request.POST.get("sold_Quantity"))
#             sale.count_sold = sale.count_sold + qty
#             sale.save()
#             sale = Product.objects.only('stock').get(baseentity_ptr = request.POST.get('Product_id'))
#
#         else:
#             HttpResponse("Error Occured")
#
#         context = [{
#            'Product_id':Product.objects.only('product_name').get(baseentity_ptr = request.POST.get('Product_id')),
#             'qty' : request.POST.get("sold_Quantity"),
#             'price' : request.POST.get("price"),
#             'total_price' : request.POST.get("total_price"),
#             'date' : request.POST.get('date_time'),
#             'namount' : request.POST.get('namount'),
#             'event' : Event.objects.only('event_name').get(id = request.POST.get('Event_Name'))
#         }]
#
#         return render(request,'invoice/invoice.html',{'context':context})
#     return render(request,'orders/add_order.html',{'form':form,'data':Product.objects.all()})

def invoice(request):
    return render(request,'invoice/invoice.html',{'context':Invoice.objects.all()})
def manageOrders(request):
    return render(request,'invoice/invoice.html',{'context':Invoice.objects.all()})
def viewOrder(request):
    return render(request,'orders/list_of_order.html',{'context':OrderItem.objects.all()})

def load_price(request):
    product_id = request.GET.get('product_id')
    price = Product.objects.only('Price').filter(baseentity_ptr=product_id).get()
    return render(request, 'orders/price.html', {'prices': price})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def updateOrder(request, pk):
    try:
        item = OrderItem.objects.get(id=pk)
    except ObjectDoesNotExist:
        item = None
    form = OrderItemForm(instance=item)
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('view-order')
    return render(request, 'orders/update_order.html', {'form':form})


def deleteOrder(request,pk):
    Invoice.objects.filter(baseentity_ptr=pk).delete()
    messages.success(request,"Order Deleted Successfully")
    return render(request,'orders/list_of_order.html',{'context':Invoice.objects.all()})
