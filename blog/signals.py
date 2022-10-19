from django.db.models.signals import post_save, pre_save, pre_delete, m2m_changed
from django .dispatch import receiver
from .models import Blog, BlogStatistic
from django.utils.text import slugify

@receiver(post_save, sender=Blog)
def post_save_fun(sender, instance, *args, **kwargs):
    # if created:
        BlogStatistic.objects.create(
            blog=instance,
        )


@receiver(pre_save, sender=Blog)
def pre_save_fun(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


@receiver(pre_delete, sender=Blog)
def pre_delete_fun(sender, instance, *args, **kwargs):
    blog_stat = BlogStatistic.objects.get(blog = instance)
    if blog_stat.read_count > 15 :
        raise Exception('15den boyuk')


# @receiver(m2m_changed, sender = Blog.tags.through)
# def m2m_changed_func(sender, instance, action, *args, **kwargs):
