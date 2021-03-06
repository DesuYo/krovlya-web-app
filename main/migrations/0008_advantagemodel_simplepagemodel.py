# Generated by Django 2.0.4 on 2018-04-27 22:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180427_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvantageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('subTitle', models.CharField(max_length=50)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SimplePageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=25)),
                ('headerImage', models.ImageField(default='default.png', upload_to='')),
                ('content', ckeditor.fields.RichTextField()),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
    ]
