# Generated by Django 4.2.1 on 2023-06-26 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]