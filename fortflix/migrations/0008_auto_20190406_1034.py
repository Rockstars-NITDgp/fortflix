# Generated by Django 2.2 on 2019-04-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortflix', '0007_auto_20190406_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('DEFAU', 'Default'), ('SCIFI', 'Science-Fiction'), ('THRILL', 'Thrillers'), ('FAMIL', 'Family'), ('XKIDS', 'Kids'), ('CRIME', 'Crime'), ('HORRO', 'Horror'), ('ROMAN', 'Romance'), ('DRAMA', 'Drama'), ('DOCUM', 'Documentary'), ('STAND', 'StandUp Comedy'), ('ADVER', 'Advertisement'), ('ANIME', 'Anime'), ('SPORTS', 'Sports'), ('ACTIO', 'Action')], default='DEFAU', max_length=15),
        ),
    ]
