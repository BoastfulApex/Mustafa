# Generated by Django 4.1.1 on 2022-12-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_paind_order_paid_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stop_list',
            field=models.BooleanField(default=False),
        ),
    ]