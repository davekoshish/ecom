from rest_framework import routers, urlpatterns
from . import views
from django.urls import path , include

router = routers.DefaultRouter()
router.register(r'',views.ProductViewSet)

urlpatterns=[
    path('',include(router.urls))
]