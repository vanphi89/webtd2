# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire_article',
            name='phone',
            field=models.CharField(max_length=15, default='0'),
        ),
        migrations.AlterField(
            model_name='userpostt',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
