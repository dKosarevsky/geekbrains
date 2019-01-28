from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Name", max_length=64, unique=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=256)
    image = models.ImageField(upload_to='products_image', blank=True)
    short_desc = models.CharField(verbose_name='short_desc', max_length=60, blank=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(verbose_name='sklad', default=0)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        # a = self.category_id
        # b = self.category_id
        return "{} ({})".format(self.name, self.category.name)
