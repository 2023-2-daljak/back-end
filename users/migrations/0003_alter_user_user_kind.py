# Generated by Django 4.2.6 on 2023-10-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_kind',
            field=models.CharField(choices=[('client', 'Client'), ('student', 'Student')], max_length=10),
        ),
    ]
