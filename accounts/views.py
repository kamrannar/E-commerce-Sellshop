from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.models import Cart, Cart_item,Wishlist
from product.models import Product
from django.db.models import Q
from django.utils.translation import gettext as _


class MyAccount(View):
    template_name = 'my-account.html'
    form_class = BillingForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_account')
        else:
            messages.warning(request, 'Please correct the errors below')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.request.user.id)
        return context


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home'
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():            
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_emails=User.objects.all().values_list('email', flat=True)
            if form.data['email'] in user_emails:
                messages.error(request, _("Email is already registered"))
                return HttpResponseRedirect(self.request.path_info)
            else:   
                user.set_password(
                    form.cleaned_data["password"]
                )
                user.save()
                Cart.objects.create(user_id=User.objects.all().last())
                
                messages.success(request, _("Successfully registered "+"\N{pinched fingers}")
                )
                return redirect('login')
        return HttpResponseRedirect(self.request.path_info)


def checkout(request):
    form = BillingForm()
    form2 = Different_shippingForm()
    if request.method == "POST":
        form = BillingForm(request.POST)
        form2 = Different_shippingForm(request.POST)
        if form2.is_valid():
            form2.save()
            form2 = Different_shippingForm()
        if form.is_valid():
            form.save()
            form = BillingForm()
        return redirect('order_complete')

    return render(request, 'checkout.html', {'form': form, 'form2': form2})


class CartView(ListView):
    model = Cart_item
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return redirect('/accounts/cart/')

class WishlistView(ListView):
    model = Wishlist
    template_name = 'wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlist_items'] = Wishlist.objects.filter(
            user_id_wishlist=self.request.user)

        return context



        