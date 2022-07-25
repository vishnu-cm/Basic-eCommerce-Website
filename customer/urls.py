from django.urls import path
from .import views


urlpatterns = [


    path('logincustomer', views.logincustomer, name='logincustomer'),
    path('registercustomer',views.registercustomer, name='registercustomer'),
    path('logout', views.logoutcustomer, name='logoutcustomer'),    
    path('products/<int:product_id>',views.products,name='products'),
    path('products', views.homepage, name='products'),
    path('viewproductdetails/<int:product_id>',views.viewproductdetails,name='viewproductdetails'),
    path('viewcustomercart', views.viewcustomercart, name='viewcustomercart'),
    path('addtocart', views.addproducttocart, name='addtocart'),
    path('removefromcart', views.removeproductfromcart, name='removefromcart'),
    path('viewcustomercart', views.viewcustomercart, name='viewcustomercart'),
    path('removefromcartpage/<int:cart_item_id>', views.removeproductcartpage, name='removeproductcartpage'),
    path('checkoutcustomer', views.checkoutcustomer, name='checkoutcustomer'),
    path('markpaymentsuccess', views.markpaymentsuccess, name='markpaymentsuccess'),

        
]
