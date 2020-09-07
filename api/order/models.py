from django.db import models
from api.user.models import CustomUser
from api.product.models import Product


class Order(models.Model):
    models.ForeignKey(CustomUser, null=True, blank=True, verbose_name=(
        ""), on_delete=models.CASCADE)
    product_names = models.CharField(max_length=500)
    total_products = models.CharField(max_length=500, default=0)
    transaction_id = models.CharField(max_length=500, default=0)
    total_amount = models.CharField(max_length=50, default=0)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name
