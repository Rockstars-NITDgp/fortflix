# Generated by Django 2.2 on 2019-04-05 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortflix', '0002_remove_customuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mobile',
            field=models.IntegerField(default=9876543210, validators=[django.core.validators.MaxValueValidator(9999999999)]),
            preserve_default=False,
        ),
    ]
