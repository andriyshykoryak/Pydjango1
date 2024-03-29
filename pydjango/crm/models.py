from django.db import models

# Create your models here.
class Order(models.Model):
    oreder_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200,verbose_name='Name')
    order_phone = models.CharField(max_length=200,verbose_name='Phone')
    def __str__(self) -> str:
        return self.order_name
    class Meta:
        verbose_name='Order'
        verbose_name_plural = 'Orders'