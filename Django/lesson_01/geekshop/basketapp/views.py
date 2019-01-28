from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse
from django.http import JsonResponse

from basketapp.models import Basket
from mainapp.models import Product
from mainapp.views import get_basket


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

    content = {'title': title, 'basket_items': basket_items, }

    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    old_basket_item = Basket.objects.filter(user_id=request.user.id, product_id=product.id)

    if old_basket_item:
        old_basket_item[0].quantity += 1
        old_basket_item[0].save()
    else:
        new_basket_item = Basket.objects.create(
            user_id=request.user.id,
            product_id=product.id,
            quantity=1
        )
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(reverse('basket:view'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/includes/basket_list.html', content)

        return JsonResponse({'result': result})