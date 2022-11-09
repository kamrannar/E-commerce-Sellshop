from django.shortcuts import render
from .models import Blog,Comment
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormMixin
from .forms import CommentsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from product.models import Category
class BlogList(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'
    paginate_by = 6
    queryset = Blog.objects.order_by('-id')
    

class BlogDetail(FormMixin, DetailView):
    model = Blog
    template_name='single-blog.html'
    form_class=CommentsForm


    def blog_detail_view(self,slug):
        blog = self.objects.filter(slug=slug)
        context = {'blog': blog}
        return render(self, self.template_name, context=context) 
    
    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['blog_comment']=Comment.objects.filter(blog_id=self.object.id)
        context['blog_related'] = Blog.objects.filter(
            category=self.object.category).exclude(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Blog.objects.order_by('-created_at')[:3]
        return context

    def get_queryset(self, *args, **kwargs):
        categories = self.request.GET.get('category')
        if categories:
            queryset = Blog.objects.filter(category=categories)
        else:
            queryset = Blog.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):   
        
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog_id = Blog.objects.get(
                slug=self.kwargs['slug'])
            form.save()
            return HttpResponseRedirect(self.request.path_info)
        else:messages.warning(request, 'Please correct the errors below')