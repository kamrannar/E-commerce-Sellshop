# Generated by Django 4.1.1 on 2022-11-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_wishlist_user_id_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='emails',
        ),
    ]
