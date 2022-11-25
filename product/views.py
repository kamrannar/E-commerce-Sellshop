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
from django.db.models import Q
class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['best_brand'] = Product_version.objects.order_by(
            '-product_view')[0]
        if len(Product_version.objects.filter(color_id=self.request.GET.get('color_id')))>0:
            context['product_versions']=Product_version.objects.filter(color_id=self.request.GET.get('color_id'))
        return context

    def get_queryset(self, *args, **kwargs):
        size = self.request.GET.get('product_size')
        brands = self.request.GET.get('brand_id')
        categoriess = self.request.GET.get('category_id')
        colors = self.request.GET.get('color_id')
        minPrice= self.request.GET.get('minPrice')
        maxPrice= self.request.GET.get('maxPrice')
        if size:
            queryset = Product.objects.filter(product_size=size)
        elif brands:
            queryset = Product.objects.filter(brand_id=brands)
        elif colors:
            queryset = Product.objects.filter(product_color=colors)
        elif categoriess:
            queryset = Product.objects.filter(category_id=categoriess)
            print(queryset)

        elif (minPrice and maxPrice):
            print(111111111111111111111111111)
            queryset = Product.objects.filter(pro__discount_price__range=(minPrice, maxPrice)).distinct
            print(queryset)
        elif minPrice:
            queryset = Product.objects.filter(Q(pro__discount_price__gte = minPrice))
        else:
            queryset = Product.objects.all()
        return queryset


class SingleProductView(FormMixin, DetailView):
    model = Product_version
    template_name = 'single-product.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(SingleProductView, self).get_context_data(**kwargs)
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
        context['sum'] = 0
        view_object = Product_version.objects.get(slug=self.kwargs['slug'])
        view_object.product_view = view_object.product_view+1
        view_object.save()
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
    # heavy_process.delay()
    return redirect('/')
