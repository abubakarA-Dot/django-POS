from base.models.product import Product
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import Group,Permission
from django.contrib import messages
from base.forms.group_form import UpdateGroupForm


def startGroup(request):
    val = request.POST.get('userCreate')
    if request.method == "POST": 
        # name = 
        # return HttpResponse(name)
        gname = request.POST.get('groupName')
        
        g1 = Group.objects.create(name=gname)

        checkBox ={'userCreate':'add user','userUpdate':'change user','userView':'view user','userDelete':'delete user',
                    'groupCreate':'add group','groupUpdate':'change group','groupView':'view group','groupDelete':'delete group',
                    'categoryCreate':'add category','categoryUpdate':'change category','categoryView':'view category','categoryDelete':'delete category',
                    'inventoryCreate':'add inventory','inventoryUpdate':'change inventory','inventoryView':'view inventory','inventoryDelete':'delete inventory',
                    'productsCreate':'add product','productsUpdate':'change product','productsView':'view product','productsDelete':'delete product',
                    'ordersCreate':'add order','ordersUpdate':'change order','ordersView':'view order','ordersDelete':'delete order',
                    'ordersCreate':'add order','ordersUpdate':'change order','ordersView':'view order','ordersDelete':'delete order',
                }
        
        for key,value in checkBox.items():
            if key in request.POST:
                can_fm_list = Permission.objects.get(name='Can '+value)
                g1.permissions.add(can_fm_list)





        # if 'userUpdate' in request.POST:
        #     can_fm_list = Permission.objects.get(name='Can change user')
        #     g1.permissions.add(can_fm_list)
        # if 'userView' in request.POST:
        #     can_fm_list = Permission.objects.get(name='Can view user')
        #     g1.permissions.add(can_fm_list)
        # if 'userUpdate' in request.POST:
        #     can_fm_list = Permission.objects.get(name='Can delete user')
        #     g1.permissions.add(can_fm_list)
        #add: user.has_perm('foo.add_bar')
        
        return render(request,'groups/list_of_group.html',{'group':Group.objects.all(),'message':'Group Added Successfully'})
    return render(request,'groups/add_group.html')  

def manageGroup(request):
    return render(request,'groups/list_of_group.html',{'group':Group.objects.all()})

def updateGroup(request,group_id):
    group_object = get_object_or_404(Group, pk=group_id)
    group_form = UpdateGroupForm(instance = group_object)
    if request.method == 'POST':
        group_form = UpdateGroupForm(request.POST,instance=group_object)
        if group_form.is_valid():
            group_form.save()
            return redirect('manageGroup')
    return render(request, "groups/update_group.html", {'form':group_form})

def deleteGroup(request,pk):
    Group.objects.filter(name=pk).delete()
    messages.success(request,"Group Deleted Successfully")
    return render(request,'groups/list_of_group.html',{'group':Group.objects.all(),'message':'ali'})
