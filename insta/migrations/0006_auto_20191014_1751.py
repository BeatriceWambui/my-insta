# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20191014_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='photos/'),
        ),
    ]
