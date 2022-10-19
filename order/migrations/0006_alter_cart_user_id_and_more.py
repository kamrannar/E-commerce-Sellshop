# Generated by Django 4.1.1 on 2022-10-18 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_product_version_color_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_alter_cart_items_product_version_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart_items',
            name='product_version_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product_version'),
        ),
    ]