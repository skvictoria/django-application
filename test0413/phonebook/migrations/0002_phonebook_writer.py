# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonebook',
            name='writer',
            field=models.CharField(max_length=200, default='admin'),
            preserve_default=False,
        ),
    ]
