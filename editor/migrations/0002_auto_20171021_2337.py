# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(default='previews/none/no_preview.png', upload_to='previews/')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='images/none/no_image.png', upload_to='images/'),
        ),
    ]
