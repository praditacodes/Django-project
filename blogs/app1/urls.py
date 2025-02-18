from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Fixed to use blog_id
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),  # Fixed to use blog_id
    path('product_list',views.product_list, name='product_list'),
]
