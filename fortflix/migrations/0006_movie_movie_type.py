# Generated by Django 2.2 on 2019-04-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortflix', '0005_auto_20190406_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(choices=[('BASIC', 'Basic'), ('PAID', 'Paid')], default='Paid', max_length=5),
        ),
    ]