from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('food/',views.food),
    path('about/',views.about),
    path('about_us_more/', views.about_us_more, name='about_us_more'),
    path('booktable/',views.booktable),
    path('contact/',views.contact),
    path('faqs/',views.faqs),
    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),
    path('cart/',views.cart),
    path('history/',views.orderhistory),
    path('profile/',views.myprofile),
    path('showcart/',views.showcart),
    path('productcart/',views.cartforproduct),
    path('order/',views.order),
    path('portfolio/', views.portfolio),

]
