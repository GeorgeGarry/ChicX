# Generated by Django 4.2.4 on 2024-06-07 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_colors_remove_product_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsize',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size',
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]
