# Generated by Django 4.0.5 on 2022-06-17 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_created_date_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(verbose_name=datetime.datetime.now),
        ),
    ]
