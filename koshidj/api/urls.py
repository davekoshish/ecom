from django.urls import path , include
from rest_framework.authtoken import views
from .views import home

urlpatterns=[
#this the root route of the api app and we are rendering home funtion here . the name parameter is optional
    path('',home,name='api.home'),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('payment/',include('api.payment.urls')),
    path('order/',include('api.order.urls')),
]
