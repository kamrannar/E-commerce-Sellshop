from django.shortcuts import render
from blog.models import Blog
from product.models import Product_version, Product
from accounts.models import Cart_item,Cart
from .forms import ContactForm
from django.views.generic import *
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from accounts.views import *
class home(TemplateView):
    model = Product_version
    template_name = 'index.html'

    # heavy_process()
    def get_context_data(self, *args, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        if not Cart.objects.filter(user_id=User.objects.all().last()):
            Cart.objects.create(user_id=User.objects.all().last())
        context['price'] = Product_version.objects.order_by('price')
        context['blog'] = Blog.objects.order_by('-id')[:3]
        context['new_products'] = Product.objects.order_by('-created_at')[:6]
        context['new_productsss'] = Product.objects.all()
        context['sum'] = 0
        for i in Cart_item.objects.filter(cart_id=self.request.user.id):
            context['sum'] += float(i.product_version_id.discount_price)
        
        return (context)


def about(request):
    return render(request, 'about.html')


class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message successfully sent')
            return HttpResponseRedirect(self.request.path_info)

        return render(request, self.template_name, {'form': form})


def error(request):
    return render(request, 'error-404.html')
    
class SearchResultsView(ListView):
    model = Product
    template_name = '../../product/templates/product-list.html'
    context_object_name = 'products'
    def get_queryset(self):
        query = self.request.GET.get('search')
        products=Product.objects.filter(Q(title__icontains=query))
        return products