# Generated by Django 3.2.20 on 2023-07-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=1000),
        ),
    ]
