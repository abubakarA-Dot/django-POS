from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from base.models.category import Category
from base.forms.category_form import CreateCategoryForm, UpdateCategoryForm


# @method_decorator(login_required(login_url='/login/'), name='dispatch')
# class CategoryCreateView(SuccessMessageMixin, CreateView):
#     template_name = 'category/create_category.html'
#     success_message = "Category successfully created!"
#     model = Category
#     form_class = CategoryForm
#     success_url = '/create-category/'

def create_category(request):
    create_cat = CreateCategoryForm()
    if request.method == 'POST':
        create_cat = CreateCategoryForm(request.POST)
        if create_cat.is_valid():
            create_cat.save()
            return redirect('category_list')
    context = {
        'category': create_cat
    }
    return render(request, 'category/create_category.html', context)



def update_category(request, cat_id):
    cat_update = get_object_or_404(Category, id=cat_id)
    update_cat_form = UpdateCategoryForm(instance=cat_update)
    if request.method == 'POST':
        update_cat_form = CreateCategoryForm(request.POST, instance=cat_update)
        if update_cat_form.is_valid():
            update_cat_form.save()
            return redirect('category_list')
    context = {
        'update_category': update_cat_form
    }
    return render(request, 'category/update_category.html', context)



# @method_decorator(login_required(login_url='/login/'), name='dispatch')
# class CategoryListView(ListView):
#     template_name = 'category/category_list.html'
#     model = Category
#     context_object_name = 'category'
#     paginate_by = 10
@login_required(login_url='login')
def categories(request):
    all_categories = Category.objects.all()
    cat_count = all_categories.count()
    context = {
        'all_categories':all_categories,
        'cat_count': cat_count
    }
    return render(request, 'category/category_list.html', context)


# class CategoryUpdateView(UpdateView):
#     template_name = 'category/create_category.html'
#     model = Category
#     form_class = CreateCategoryForm
#     success_url = '/category/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryDeleteView(DeleteView):
    template_name = 'category/category_confirm_delete.html'
    model = Category
    success_url = '/category/'
