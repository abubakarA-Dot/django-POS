from base.models.Invoice import Event
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from datetime import date
from base.models import product
from base.models.product import Product
from base.forms.product_form import ProductForm, UpdateProductForm
from django.db.models import Q



# @method_decorator(login_required(login_url='/login/'), name='dispatch')
# class CreateProductView(SuccessMessageMixin, CreateView):
#     template_name = 'product/add_product.html'
#     model = Product
#     form_class = ProductForm
#     success_message = 'Product has been created'
#     success_url = '/product_list/'

def create_product(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_list')
    context = {
        "productForm": product_form
    }
    return render(request, 'product/add_product.html', context)


def update_product(request, product_id):
    product_model = get_object_or_404(Product, id=product_id)
    update_product_form = UpdateProductForm(instance=product_model)
    if request.method == 'POST':
        update_product_form = ProductForm(request.POST, instance=product_model)
        if update_product_form.is_valid():
            update_product_form.save()
            return redirect('product_list')
    context = {
        "updateProductForm": update_product_form
    }
    return render(request, 'product/update_product.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/delete_product.html')

def search_products(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        search_button = request.GET.get('submit')
        if query is not None:
            condition = Q(product_name__icontains=query) | Q(product_uuid__icontains=query) | Q(expiry_date__icontains=query) | Q(
                stock__icontains=query) | Q(description__icontains=query) 
            final_result = Product.objects.filter(condition).distinct()
            context = {
                'final_result':final_result,
                'search_button': search_button
            }
            return render(request, 'product/search_product.html', context)
        else:
            return render(request, 'product/list_of_product.html')
    else:
        return render(request, 'product/list_of_product.html')



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProductListView(ListView):
    template_name = 'product/list_of_product.html'
    model = Product
    context_object_name = 'product'


def expireProduct(request):
    x = []
    now = date.today()
    exp = Product.objects.all()
    for ex in exp:
        end = ex.expiry_date
        if (end - now).days <5:
            x.append(ex)        
    #return render(request, 'product/list_of_product.html',{'lowproduct':Product.objects.order_by('stock').all()})
    return render(request, 'product/list_of_product.html',{'expireProducts':x})



def lowProduct(request):
    return render(request, 'product/list_of_product.html',{'lowproduct':Product.objects.order_by('stock').all()})

def topSellingproduct(request):
    return render(request, 'product/list_of_product.html',{'topSellingproduct':Product.objects.all().order_by('-count_sold')[:10] })
def lowSellingproduct(request):
    return render(request, 'product/list_of_product.html',{'lowSellingproduct':Product.objects.all().order_by('count_sold')[:10] })

def eventSellingproduct(request):
    
    if request.method == "POST":
        return HttpResponse(request.POST.get('event'))
        return render(request, 'product/Event.html',{ 'lowSellingproduct':Product.objects.filter(product_name = "HP").order_by('-count_sold')[:10]})
    #'lowSellingproduct':Product.objects.filter(product_name = "HP").order_by('-count_sold')[:10]
    return render(request, 'product/Event.html',{ 'event':Event.objects.all()})
