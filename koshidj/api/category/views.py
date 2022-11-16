from rest_framework import viewsets
from .serializer import CategorySerializer
from .models import Category

#this view set it to show or push all the categoryies we have in the model
class CategoryViewSet(viewsets.ModelViewSet):
    #here we are modeling the viewset 
    queryset = Category.objects.all().order_by('name')
    #category is a model class which is used here to accessing all the elements of of Category and stored in queryset
    # now query set has a bulk of data or we can say it has python native data
    #  
    serializer_class =CategorySerializer

