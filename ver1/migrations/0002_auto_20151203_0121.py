# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ver1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='optional_image',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
