# Generated by Django 4.2.4 on 2024-06-07 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]