from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name_plural = 'Categories'
        
        
class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField(max_length=1000)
    owner = models.ForeignKey(User, related_name='expense_user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='expense_category', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.category)
    
    class Meta :
        ordering : ['-date']



    