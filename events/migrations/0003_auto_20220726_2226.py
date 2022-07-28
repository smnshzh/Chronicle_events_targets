# Generated by Django 3.2.8 on 2022-07-26 17:56

import datetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20220726_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='recordDate',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 26, 22, 26, 13, 6971), verbose_name='زمان ذخیره'),
        ),
        migrations.AlterField(
            model_name='messageerror',
            name='time',
            field=django_jalali.db.models.jDateTimeField(default=datetime.datetime(2022, 7, 26, 22, 26, 13, 13967)),
        ),
    ]
