# Generated by Django 4.1.1 on 2022-12-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_phone',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]