# Generated by Django 5.1 on 2024-08-24 13:14

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_aboutview'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutview',
            name='my_about',
            field=models.CharField(default=builtins.dir, max_length=50),
            preserve_default=False,
        ),
    ]