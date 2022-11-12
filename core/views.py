from django.shortcuts import render
from blog.models import Blog
from product.models import Product_version, Product
from accounts.models import Cart_item
from .forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect
from sellshop.tasks import heavy_process
from django.core.mail import send_mail
from django.conf import settings
class home(TemplateView):
    model = Product_version
    template_name = 'index.html'
    # heavy_process()
    def get_context_data(self, *args, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        context['price'] = Product_version.objects.order_by('price')
        context['blog'] = Blog.objects.order_by('-id')[:3]
        context['new_products'] = Product.objects.order_by('-created_at')[:6]
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
        print(self.request.user)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.request.path_info)
        else:
            messages.warning(request, 'Please correct the errors below')

        return render(request, self.template_name, {'form': form})


def error(request):
    return render(request, 'error-404.html')
