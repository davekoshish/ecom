from nturl2path import url2pathname
from django.urls import path,include
from . import views

urlpatterns = [
    path('gettoken/<str:id>/<str:token>',views.generate_token,name="token.generate"),
    path('process/<str:id>/<str:token>',views.process_payment,name="payment.process"),
]
