# Generated by Django 4.0.5 on 2022-06-22 13:54

import autoslug.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_image_phone_lte_exists_phone_name_phone_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 22, 13, 54, 42, 95577, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name'),
        ),
    ]
