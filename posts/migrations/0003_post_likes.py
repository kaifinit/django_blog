# Generated by Django 5.0.3 on 2024-03-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
