from unicodedata import category
from sellshop.tasks import heavy_process
from .models import *
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from product.api.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from . forms import *
import json

class product_list(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(product_list, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['product_versions'] = Product_version.objects.all()
        context['brands'] = Brand.objects.all()
        context['sizes'] = Size.objects.all()
        context['colors'] = Color.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        size = self.request.GET.get('product_size')
        brands = self.request.GET.get('brand_id')
        categories = self.request.GET.get('category_id')
        colors = self.request.GET.get('product_color')
        if size:
            queryset = Product.objects.filter(product_size=size)
        elif brands:
            queryset = Product.objects.filter(brand_id=brands)
        elif colors:
            queryset = Product.objects.filter(product_color=colors)
        elif categories:
            queryset = Product.objects.filter(category_id=categories)
        else:
            queryset = Product.objects.all()
        return queryset


class single_product(FormMixin, DetailView):
    model = Product_version
    template_name = 'single-product.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):

        context = super(single_product, self).get_context_data(**kwargs)
        context['image'] = Image.objects.filter(
            product_image=self.object).first().images.url
        context['image2'] = Image.objects.filter(
            product_image=self.object).last().images.url
        context['products_version'] = Product_version.objects.filter(
            product=self.object.product)

        context['products_version_related'] = Product_version.objects.filter(
            product=self.object.product).exclude(slug=self.kwargs['slug'])
        context['image_related'] = Product_version
        context['tag'] = Tag.objects.filter(tags=self.object.product.id)
        context['reviews'] = Review.objects.filter(products_id=self.object.id)
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.products_id = Product_version.objects.get(
                slug=self.kwargs['slug'])
            my_form.save()
            return HttpResponseRedirect(self.request.path_info)
        else:
            messages.warning(request, 'Please correct the errors below')

@api_view(["GET", "POST"])
def product_listt(request, format=None):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({'product': serializer.data})

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def call_heavy_process(request):
    heavy_process.delay()
    return redirect('home')
