# Generated by Django 5.1.7 on 2025-03-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
