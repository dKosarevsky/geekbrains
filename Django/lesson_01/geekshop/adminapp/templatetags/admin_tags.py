from django import template
from django.conf import settings


register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(product_img_path):
    if not product_img_path:
        product_img_path = 'product_images/default.jpg'

    return f"{settings.MEDIA_URL}{product_img_path}"


def media_folder_users(avatar_path):
    if not avatar_path:
        avatar_path = 'users_avatars/default.jpg'

    return f"{settings.MEDIA_URL}{avatar_path}"


register.filter('media_folder_users', media_folder_users)