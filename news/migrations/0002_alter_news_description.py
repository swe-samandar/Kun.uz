# Generated by Django 5.1.7 on 2025-03-20 07:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
