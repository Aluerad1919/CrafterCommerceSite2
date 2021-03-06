from django.urls import path, include
from.import views, models


urlpatterns = [
    path('', views.index),
    # Login and Registration paths
    path('log', views.login),
    path('CrafterMall/Signup', views.registerform),
    path('register', views.register),
    path('logout', views.logout),
    # User account Paths
    path('CrafterMall/Account/<int:val>', views.user_account, name="user_account"),
    path('CrafterMall/Add_Address/<int:val>', views.address_form),
    path('add_address', views.add_address),
    path('CrafterMall/edit_address/<int:val>', views.edit_form),
    path('edit_address/<int:val>',views.edit_address),
    path('delete/<int:val>', views.delete_address),
    # User Store Paths
    path('CrafterMall/<int:val>/Store_Front', views.store_front, name='store_front'),
    path('opening_store/<int:val>', views.opening_store),
    path('CrafterMall/<int:val>/Add_a_Craft', views.add_product, name='add_prod'),
    path('add_craft_product', views.post_new_product),
    path('delete_cloth/<int:val>', views.delete_cloth),
    path('delete_leather/<int:val>', views.delete_leather),
    path('delete_metal/<int:val>', views.delete_metal),
    path('delete_wood/<int:val>', views.delete_wood),
    path('delete_jewel/<int:val>', views.delete_jewel),
    path('delete_digi/<int:val>', views.delete_digi),
    path('show_product/<str:mats>/<int:val>', views.show_product),
]   