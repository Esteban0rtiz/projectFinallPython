from django.db import models

# Create your models here.

class Shop(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nombre Producto")
    size=models.CharField(max_length=100, verbose_name="Talla")
    image=models.ImageField(verbose_name="imagen", upload_to="shop")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Shop"
        verbose_name_plural="Compras"
        ordering=['-created']

    def __str__(self):
        return self.name
