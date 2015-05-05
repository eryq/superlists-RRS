# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list_'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='List_',
            new_name='List',
        ),
    ]
