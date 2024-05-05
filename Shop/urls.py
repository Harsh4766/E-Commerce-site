from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shop'),
    path('about',views.about,name='about'),
    path('contact',views.contactus,name='contact'),
    path('tracker',views.tracker,name='tracker'),
    path('search',views.search,name='search'),
    path('productview/<int:myid>',views.productview,name='productview'),
    path('checkout',views.checkout,name='checkout'),
    path('buyproduct',views.buyproduct,name='buyproduct'),
    path('payment-success',views.success,name='payment-success')
]
