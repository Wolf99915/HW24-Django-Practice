# Generated by Django 3.1.1 on 2023-01-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_categoryproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]