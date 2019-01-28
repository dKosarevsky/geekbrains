from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

User = get_user_model()


class Basket(models.Model):
    product = models.ForeignKey('mainapp.Product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def _get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(_get_product_cost)

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user_id=self.user.id)
        return items.aggregate(total=Sum('quantity'))['total']

    @property
    def total_cost(self):
        items = Basket.objects.filter(user_id=self.user.id)
        return sum(list(map(lambda x: x.product_cost, items)))

