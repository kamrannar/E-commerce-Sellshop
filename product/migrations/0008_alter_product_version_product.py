# Generated by Django 4.1.1 on 2022-11-22 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_version_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_version',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pro', to='product.product'),
        ),
    ]