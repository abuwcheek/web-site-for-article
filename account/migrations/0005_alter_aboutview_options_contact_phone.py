# Generated by Django 5.1 on 2024-08-24 14:37

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_aboutview_my_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutview',
            options={'verbose_name': 'About'},
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=builtins.dir, max_length=15),
            preserve_default=False,
        ),
    ]