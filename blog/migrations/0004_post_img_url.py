# Generated by Django 4.2.2 on 2023-06-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
