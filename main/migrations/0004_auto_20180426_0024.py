# Generated by Django 2.0.4 on 2018-04-25 21:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180425_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidemodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
