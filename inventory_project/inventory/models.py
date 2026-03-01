from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InventoryItem(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'items')
    name = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.CharField(max_length = 100)
    date_added = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name
    


class InventoryChangeLog(models.Model):
    item = models.ForeignKey(
        InventoryItem, on_delete = models.CASCADE, related_name = 'changes'
    )

    changed_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    previous_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.item.name} has been updated'