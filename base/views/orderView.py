from django.http import request
from base.forms.invoice_form import InvoiceForm

from django.http.response import HttpResponse
from base.models.Invoice import Event
from django.core.checks import messages
from base.models import product
from base.models.product import Product
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from base.models.Invoice import Invoice
from django.contrib import messages
from django.contrib.auth.models import User
def add_order(request):
    form = InvoiceForm()
    if request.method == "POST":
        form = InvoiceForm(request.POST or None)
        if form.is_valid:
            form.save()
            #name = Product.objects.only('product_name').get(baseentity_ptr = request.POST.get('Product_id'))
            sale = Product.objects.only('stock').get(baseentity_ptr = request.POST.get('Product_id'))
            qty = int(request.POST.get("sold_Quantity"))
            sale.count_sold = sale.count_sold + qty
            sale.save()
            sale = Product.objects.only('stock').get(baseentity_ptr = request.POST.get('Product_id'))
            
        else:
            HttpResponse("Error Occured")    

        context = [{
           'Product_id':Product.objects.only('product_name').get(baseentity_ptr = request.POST.get('Product_id')),
            'qty' : request.POST.get("sold_Quantity"),
            'price' : request.POST.get("price"),
            'total_price' : request.POST.get("total_price"),
            'date' : request.POST.get('date_time'),
            'namount' : request.POST.get('namount'),
            'event' : Event.objects.only('event_name').get(id = request.POST.get('Event_Name'))
        }]
        
        return render(request,'invoice/invoice.html',{'context':context})
    return render(request,'orders/add_order.html',{'form':form,'data':Product.objects.all()})

def invoice(request):
    return render(request,'invoice/invoice.html',{'context':Invoice.objects.all()})
def manageOrders(request):
    return render(request,'invoice/invoice.html',{'context':Invoice.objects.all()})
def viewOrder(request):
    return render(request,'orders/list_of_order.html',{'context':Invoice.objects.all()})

def load_price(request):
    product_id = request.GET.get('product_id')
    price = Product.objects.only('Price').filter(baseentity_ptr=product_id).get()
    return render(request, 'orders/price.html', {'prices': price})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def updateOrder(request,pk):
   invoice = get_object_or_404(Invoice, pk=pk)  # baseentity_ptr
   form = InvoiceForm(instance = invoice) 
   if request.method == 'POST':
       form = InvoiceForm(request.POST, instance=invoice)
       if form.is_valid():
        form.save()
        return redirect('view-order')
   return render(request,'orders/update_order.html',{'form':form})

def deleteOrder(request,pk):
    Invoice.objects.filter(baseentity_ptr=pk).delete()
    messages.success(request,"Order Deleted Successfully")
    return render(request,'orders/list_of_order.html',{'context':Invoice.objects.all()})
