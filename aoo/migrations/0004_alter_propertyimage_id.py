# Generated by Django 5.2.1 on 2025-06-16 09:38

import django_mongodb_backend.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0003_remove_property_image_propertyimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimage',
            name='id',
            field=django_mongodb_backend.fields.ObjectIdAutoField(primary_key=True, serialize=False),
        ),
    ]
