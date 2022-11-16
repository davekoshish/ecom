from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    #this method here will give the catogory a name 
    def __str__(self) -> str:
        return self.name