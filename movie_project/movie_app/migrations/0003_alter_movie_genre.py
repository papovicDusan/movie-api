# Generated by Django 4.0.2 on 2022-02-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('HISTORICAL', 'Historical'), ('HORROR', 'Horror')], default='HISTORICAL', max_length=20),
        ),
    ]
