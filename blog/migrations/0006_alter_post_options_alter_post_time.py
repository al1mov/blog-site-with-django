# Generated by Django 4.2.2 on 2023-06-29 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_created_at_alter_post_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 29, 7, 44, 25, 150633, tzinfo=datetime.timezone.utc)),
        ),
    ]