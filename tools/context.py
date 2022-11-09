from accounts.models import Cart,Cart_item
from product.models import Image,Product_version,Category,Brand,Size,Color,Product
import requests

def main_context(request):
    context = {}
    context['images'] = Image.objects.all()
    context['categories'] = requests.get('http://127.0.0.1:8000/api/categories/').json()
    context['brands'] = Brand.objects.all()
    context['sizes'] = requests.get('http://127.0.0.1:8000/api/sizes/').json()
    context['product_versions']=requests.get('http://127.0.0.1:8000/api/product_version/').json()
    context['products']=requests.get('http://127.0.0.1:8000/api/product_list_api/').json()

    context['colors'] = requests.get('http://127.0.0.1:8000/api/colors/').json()
    if request.user.is_anonymous!=True:
        context['cart'] = Cart.objects.get(user_id=request.user)
        context['cart_items'] = Cart_item.objects.filter(
            cart_id=context['cart'])
    
    return context