from django.db import models

# Create your models here.
class product(models.Model):
    nama_product = models.CharField(max_length=100, null=True)
    satuan = models.IntegerField(default = 0)


