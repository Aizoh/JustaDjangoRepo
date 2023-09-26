from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    #HOW iTEMS APPEAR 
    class Meta:
        # db_table = ''
        # managed = True
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
    #OVERRIDE CONSTRUCTOR TO DISPLAY CATEGORIES ACCORDING TO THEIR NAMES
    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):

    #WHEN YOU DELETE A CATEGORY, ITEMS ASSOCIATED WITH IT ARE DELETED TOO
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    #AN IMAGE FIELD FOLDER TO UPLOAD TO
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    #GET AUTHENTICATED USER
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add =True)

    class Meta:
        # db_table = ''
        # managed = True
        ordering = ('category',)
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
    def __str__(self) -> str:
        return self.name