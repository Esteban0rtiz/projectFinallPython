# Generated by Django 4.2.4 on 2023-09-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_shop_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio'),
        ),
    ]