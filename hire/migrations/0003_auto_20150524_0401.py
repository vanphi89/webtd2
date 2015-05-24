# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_auto_20150523_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire_article',
            name='mode_work',
            field=models.ForeignKey(to='hire.mode_work'),
        ),
    ]
