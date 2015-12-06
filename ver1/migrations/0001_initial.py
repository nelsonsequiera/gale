# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'')),
                ('optional_image', models.ImageField(upload_to=b'')),
                ('body', models.TextField()),
            ],
        ),
    ]
