# Generated by Django 5.1 on 2024-08-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('my_location', models.CharField(max_length=500)),
                ('my_email', models.EmailField(max_length=254)),
                ('my_phone', models.CharField(max_length=15)),
                ('linkedin', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('youtube', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
