# Generated by Django 4.2.6 on 2023-11-17 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_meet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
    ]
