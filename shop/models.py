from django.utils import timezone

from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Brands(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Color(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Filter_price(models.Model):
    FILTER_PRICE=(
        ('1000 To 10000', '1000 To 10000'),
        ('10000 To 20000', '10000 To 20000'),
        ('20000 To 30000', '20000 To 30000'),
        ('30000 To 40000', '30000 To 40000'),
        ('40000 To 50000', '40000 To 50000')
    )

    price_range=models.CharField(choices=FILTER_PRICE,max_length=30)

    def __str__(self):
        return self.price_range

class Product(models.Model):
    CONDITION=(
        ('New','New'),
        ('Old','Old')
    )
    STOCK=('In Stock', 'In Stock'),('Out Of Stock','Out Of Stock')
    STATUS=('Publish','Publish'),('Draft','Draft')

    Pro_ID=models.CharField(unique=True ,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='Product_images/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITION,max_length=20)
    information=models.TextField()
    description=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=20)
    status=models.CharField(choices=STATUS,max_length=20)
    created_date=models.DateTimeField(default=timezone.now)

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_price,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
         if self.Pro_ID is None and self.created_date and self.id:
             self.Pro_ID=self.created_date.strftime('%Y%m%d')+str(self.id)
             print(self.Pro_ID)
         return super().save(*args,**kwargs)

    def __str__(self):
        return self.name
class Images(models.Model):
    image=models.ImageField(upload_to='Product_images/img')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
class Tags(models.Model):
    name=models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name