# Generated by Django 2.2 on 2019-04-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fortflix', '0003_customuser_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=0, max_digits=5)),
                ('movie_cost', models.IntegerField()),
                ('rewards', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('DEFAU', 'Default'), ('SCIFI', 'Science-Fiction'), ('THRILL', 'Thrillers'), ('FAMIL', 'Family'), ('XKIDS', 'Kids'), ('CRIME', 'Crime'), ('HORRO', 'Horror'), ('ROMAN', 'Romance'), ('DRAMA', 'Drama'), ('DOCUM', 'Documentary'), ('STAND', 'StandUp Comedy'), ('ADVER', 'Advertisement'), ('ANIME', 'Anime'), ('SPORTS', 'Sports'), ('ACTIO', 'Action')], default='DEFAU', max_length=5)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
