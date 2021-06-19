from base.forms.UserForm import UserForm, UpdateUserForm
from django.db import models
from django.db.models.query import RawQuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import Group,Permission,User
from django.contrib import messages



def startUser(request):
    form = UserForm()
    if request.method == "POST":
       User.objects.get_or_create(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            email = request.POST.get('email'),
            first_name = request.POST.get('fname'),
            last_name=request.POST.get('lname')
            )
       gname = Group.objects.get(name=request.POST.get('group'))
       user = User.objects.get(username = request.POST.get('username'))
       user.groups.add(gname)
       messages.success(request,"User Added Successfully")
       return redirect('/manageuser') 
        
    return render(request,'users/add_user.html',{'groups':Group.objects.all(),'form':form})

def manageuser(request):
    user = User.objects.filter(username='test123')
    users = User.objects.all()
    count = users.count()

    return render(request,'users/list_of_user.html',{'users':users, 'count': count}) 

def updateuser(request,user_id):
    groups = Group.objects.all()
    users = get_object_or_404(User,pk=user_id)
    update_user = UpdateUserForm(instance=users)
    if request.method == "POST":
        update_user = UpdateUserForm(request.POST,instance=users)
        if update_user.is_valid():
            update_user.save()
            messages.success(request, "Your profile is updated successfully!")
            return redirect('manageuser')
    return render(request,'users/update_user.html',{'users':users,'groups':groups, 'update_user':update_user})

def deleteuser(request,pk):
    User.objects.filter(username = pk).delete()
    messages.success(request,"User Deleted Successfully")
    return render(request,'users/list_of_user.html',{'users':User.objects.all()})

def user_profile(request, profile_id):
    user = get_object_or_404(User, pk=profile_id)
    return render(request,'users/profile.html', {'users': user})
