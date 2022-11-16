from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
   #this image has to be treated carefully here cause it doesnt give full url so we have to create it 
    image=serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False) 
    class Meta:
        model = Product
        fields=('id','name','description','is_active','stock','price','image','category')
        