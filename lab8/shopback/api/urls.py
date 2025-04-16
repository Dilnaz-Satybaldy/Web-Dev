from django.urls import path

from . import views

urlpatterns =[
    path('products/', views.get_products),
    path('products/create/', views.create_product),
    path('categories/', views.get_categories),
    path('categories/create/', views.create_category),
    path('products/<int:id>/', views.get_product_by_id),
    path('categories/<int:id>/', views.get_category_by_id),
    path('categories/<int:id>/products/', views.get_products_by_category)
    
]