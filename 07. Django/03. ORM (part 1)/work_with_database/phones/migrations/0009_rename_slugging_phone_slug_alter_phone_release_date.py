# Generated by Django 4.0.5 on 2022-06-22 21:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_rename_slug_phone_slugging_alter_phone_release_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='slugging',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 22, 21, 18, 40, 495713, tzinfo=utc)),
        ),
    ]
