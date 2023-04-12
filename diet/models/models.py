from django.db import models

 

class Product(models.Model):
    name=models.CharField(max_length=255)
    protein=models.FloatField()
    fat=models.FloatField()
    carbo=models.FloatField()
    grams=models.FloatField(default=100)
     
    
    
    def calories(self):
        calories = (self.protein*4) + (self.carbo*4)+(self.fat*9)
        return int(calories)
    
    def __str__(self) -> str:
        return self.name
    
   
        

class Diary(models.Model):
    date = models.DateField()
    name=models.CharField(max_length=100, null=True)
    products=models.ManyToManyField(Product)
    
    def calories(self):
        total_calories=0
        for product in self.products.all():
            total_calories+=product.calories()
        return total_calories