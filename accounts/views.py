from urllib import request
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


class MyAccount(View):
    template_name = 'my-account.html'
    form_class = BillingForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        user=request.user
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/my_account')
        else:messages.warning(request, 'Please correct the errors below')

        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=self.request.user.id)
        print(context['user'])
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

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data["password"]
            )
            user.save()
            return redirect('/login')
        else:
            messages.info(request, "Count not create account.")


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

