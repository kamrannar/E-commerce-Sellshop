from accounts.models import Cart,Cart_item
from product.models import Image,Category,Brand,Product_version
import requests
def main_context(request):
    context = {}
    context['images'] = Image.objects.all()
    context['categories'] = Category.objects.all()
    context['brands'] = Brand.objects.all()
    context['sizes'] = requests.get('http://127.0.0.1:8000/api/sizes/').json()
    context['product_versions']=Product_version.objects.all()
    context['products']=requests.get('http://127.0.0.1:8000/api/product_list_api/').json()
    context['popular_products']=Product_version.objects.all().order_by('product_view')[:3]
    context['bestsellers']=Product_version.objects.all().order_by('product_view')[:3]

    context['colors'] = requests.get('http://127.0.0.1:8000/api/colors/').json()
    if request.user.is_anonymous!=True:
        if Cart.objects.get(user_id=request.user):
            
            context['cart'] = Cart.objects.get(user_id=request.user)
            context['cart_items'] = Cart_item.objects.filter(
                cart_id=context['cart'])
    
    return context
