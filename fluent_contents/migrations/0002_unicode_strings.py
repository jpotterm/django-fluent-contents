# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentitem',
            name='language_code',
            field=models.CharField(editable=False, max_length=15, db_index=True, default=''),
        ),
        migrations.AlterField(
            model_name='placeholder',
            name='role',
            field=models.CharField(choices=[('m', 'Main content'), ('s', 'Sidebar content'), ('r', 'Related content')], help_text='This defines where the object is used.', max_length=1, default='m', verbose_name='Role'),
        ),
    ]
