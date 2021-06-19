from datetime import datetime
from django.http import request
from django.shortcuts import render
from django.contrib import messages
from base.models.product import Product
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from datetime import date
from base.models.category import Category
from base.models.order import Order
from base.models.tag import Tag
from base.models.inventory import Inventory
from django.contrib.auth.models import Group


def Dashboard(request):
    users = User.objects.all()
    category = Category.objects.all()
    order = Order.objects.all()
    group = Group.objects.all()
    exDate = Product.objects.all()
    x = []
    now = date.today()
    exp = Product.objects.all()
    for ex in exp:
        end = ex.expiry_date
        if (end - now).days <5:
            x.append(ex)       
            messages.info(request,"You Have Some Products That Are Going to expire ")
            break

        
    return render(request,'dashboard/dashboard.html',{'stocks':Product.objects.all(),'expire':x, 'users':users, 'category': category, 'order': order, 'group': group})



# @method_decorator(login_required(login_url='/login/'), name='dispatch')
# class Dashboard(TemplateView):

#     template_name = 'dashboard/dashboard.html'
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return render(request,'dashboard/dashboard.html',{'stocks':Product.objects.all()})

    # def get_context_data(self, *args, **kwargs):
    #     context = super(Dashboard, self).get_context_data(**kwargs)
    #     context['category'] = Category.objects.all()
    #     context['inventory'] = Inventory.objects.all()
    #     context['user'] = User.objects.all()
    #     context['tag'] = Tag.objects.all()
    #     context['product'] = Product.objects.all()
    #     return context
