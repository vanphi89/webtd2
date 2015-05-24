# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applymode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('applymode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('category_field', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['category_field'],
            },
        ),
        migrations.CreateModel(
            name='degree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('degree', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='exp_year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('exp_year', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['exp_year'],
            },
        ),
        migrations.CreateModel(
            name='hire_article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('hiring', models.CharField(max_length=250)),
                ('more_require', models.TextField(max_length=1000, blank=True)),
                ('benefit', models.TextField(max_length=1000, blank=True)),
                ('document', models.TextField(max_length=1000, blank=True)),
                ('number', models.IntegerField(default=0, blank=True)),
                ('timeover', models.DateField(default=django.utils.timezone.now, blank=True)),
                ('namecompany', models.CharField(max_length=200)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('website', models.URLField(blank=True)),
                ('infomation', models.TextField(max_length=1000, blank=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=300)),
                ('applymode', models.ForeignKey(to='hire.applymode')),
                ('category', models.ForeignKey(to='hire.category')),
                ('degree', models.ForeignKey(to='hire.degree')),
                ('exp_year', models.ForeignKey(to='hire.exp_year')),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='localwork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('localwork', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=300)),
            ],
            options={
                'ordering': ['localwork'],
            },
        ),
        migrations.CreateModel(
            name='married',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('married', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='mode_work',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('mode_work', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('salary', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['salary'],
            },
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sex', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='the_about',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('article_s', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='the_documents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('article_s', models.TextField(max_length=5000)),
                ('publication_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='userpostt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/avatas', null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField(auto_now=True)),
                ('detail', models.TextField(max_length=1000, blank=True)),
                ('skill', models.TextField(max_length=1000, blank=True)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('facebook', models.URLField(max_length=300, blank=True)),
                ('referencer', models.TextField(max_length=2000, blank=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=300)),
                ('category', models.ForeignKey(to='hire.category')),
                ('degree', models.ForeignKey(to='hire.degree')),
                ('exp_year', models.ForeignKey(to='hire.exp_year')),
                ('localwork', models.ForeignKey(to='hire.localwork')),
                ('married', models.ForeignKey(to='hire.married')),
                ('salary', models.ForeignKey(to='hire.salary')),
                ('sex', models.ForeignKey(to='hire.sex')),
            ],
        ),
        migrations.AddField(
            model_name='hire_article',
            name='language',
            field=models.ForeignKey(to='hire.language'),
        ),
        migrations.AddField(
            model_name='hire_article',
            name='localwork',
            field=models.ForeignKey(to='hire.localwork'),
        ),
        migrations.AddField(
            model_name='hire_article',
            name='mode_work',
            field=models.ForeignKey(to='hire.mode_work', blank=True),
        ),
        migrations.AddField(
            model_name='hire_article',
            name='salary',
            field=models.ForeignKey(to='hire.salary'),
        ),
        migrations.AddField(
            model_name='hire_article',
            name='sex',
            field=models.ForeignKey(to='hire.sex'),
        ),
    ]
