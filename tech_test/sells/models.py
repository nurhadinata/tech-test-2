from django.db import models
from user.models import user
from products.models import product

# Create your models here.
class selling_in_out(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    selling_in = models.IntegerField(default=0)
    selling_out = models.IntegerField(default=0)

class selling_in(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(default=0)
    no_faktur_distribusi = models.CharField(max_length=25, null=True)
    tgl_transaksi = models.DateTimeField()

class selling_out(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    stock = models.IntegerField(default=0)
    no_faktur_distribusi = models.CharField(max_length=25, null=True)
    tgl_transaksi = models.DateTimeField()




