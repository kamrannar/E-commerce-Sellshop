# Generated by Django 4.1.1 on 2022-11-05 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_cart_items_cart_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='user_id_wishlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]