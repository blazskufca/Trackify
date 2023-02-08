from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('about', views.about, name='about'),
    path('all', views.all_tracked, name='all-tracked'),
    path('register', views.register, name='register'),
    path('item/<pk>', views.product_details, name='product_details'),
    path('my-tracked/', views.my_tracked, name='my-tracked')
]