# Generated by Django 2.2 on 2019-04-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortflix', '0004_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='coins',
            field=models.IntegerField(default=0),
        ),
    ]
