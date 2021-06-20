from django.urls import path
from base.views.dashboard_view import Dashboard
from base.views.auth_view import UserLoginView, LogoutView
from base.views.category_view import    CategoryDeleteView
from base.views.inventory_view import CreateInventoryView, InventoryListView, InventoryDetailView, \
    InventoryUpdateView, InventoryDeleteView
from base.views.tag_view import CreateListTagView, TagDeleteView
from base.views.product_view import  ProductListView, eventSellingproduct,lowProduct,expireProduct, lowSellingproduct, topSellingproduct
from base.views.logout import logout_view
from base.views.pos_view import POSView, cart_add, cart_updated, cart_remove
from base.views.order_views import bulling_information_view, OrderItemView, search_orders
from base.views.group import startGroup,manageGroup,updateGroup,deleteGroup
from base.views.user import startUser, manageuser, updateuser, deleteuser, user_profile
from base.views.orderView import *
from base.views.product_view import (
    create_product, update_product, delete_product, search_products
)
from base.views.category_view import (
    create_category, update_category, categories
)
urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    # path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('create-category/', create_category, name='create_category'),
    path('update-category/<int:cat_id>/', update_category, name='update_category'),
    path('category/', categories, name='category_list'),
    # path('category/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('create-inventory/', CreateInventoryView.as_view(), name='inventory_create'),
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory-update/<pk>/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory-delete/<pk>/', InventoryDeleteView.as_view(), name='inventory_delete'),
    path('tag/', CreateListTagView.as_view(), name='create_list_tag'),
    path('tag/<pk>/', TagDeleteView.as_view(), name='tag_delete'),
    # path('create-product/', CreateProductView.as_view(), name='product_create'),
    path('product-list/', ProductListView.as_view(), name='product_list'),
    path('create-product/', create_product, name='product_create'),
    path('update-product/<int:product_id>', update_product, name='product_update'),
    path('delete-product/<int:product_id>', delete_product, name='delete_update'),
    path('search-products/', search_products, name='search_products'),
    path('cart/id/', cart_add, name='cart_add'),
    path('cart-update/<int:id>/', cart_updated, name='cart_updated'),
    path('cart-remove/<int:id>/', cart_remove, name='cart_remove'),
    path('pos/', POSView.as_view(), name='pos_view'),
    path('bulling-infromation/', bulling_information_view, name='bulling_information'),
    path('order-infromation/', OrderItemView.as_view(), name='order_information'),
    path('add_group/', startGroup, name='add_group'),
    path('manageGroup/', manageGroup, name='manageGroup'),
    path('group-update/<int:group_id>/', updateGroup, name='group_update'),
    path('group-delete/<pk>', deleteGroup, name='group_delete'),
    path('add_user/', startUser, name='add_user'),
    path('manageuser/', manageuser, name='manageuser'),
    path('user-profile/<int:profile_id>/', user_profile, name='user_profile'),


    path('user-update/<int:user_id>/', updateuser, name='user_update'),
    path('user-delete/<pk>', deleteuser, name='user_delete'),
    path('logout', logout_view, name='logout'),
    path('low-product', lowProduct, name='low-product'),
    path('expireProduct', expireProduct, name='expire-Product'),
    path('topSellingProduct', topSellingproduct, name='top-selling-Product'),
    path('lowSellingproduct', lowSellingproduct, name='low-selling-Product'),
    path('eventSellingproduct', eventSellingproduct, name='event-selling-Product'),
    # path('add_order', add_order, name='Add-order'),
    path('invoice', invoice, name='Add-order'),
    path('viewOrder', viewOrder, name='view-order'),
    path('order-update/<int:pk>/', updateOrder, name='order_update'),
    path('order-delete/<pk>/', deleteOrder, name='order_delete'),
    path('search-orders/', search_orders, name='search_orders'),
    path('load-price', load_price, name='load-price'),

    path('create_order/', create_order, name='create_order'),
    path('get_product/', get_product, name='get_product'),
    path('ajax_create_order/', ajax_order_create, name='ajax_create_order'),

]


