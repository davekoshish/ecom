from django.db.models.fields import Field
from rest_framework import serializers
from .models import Category

#serializer.py file to serialize data in JSON
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name','description')
