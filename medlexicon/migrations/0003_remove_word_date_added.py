# Generated by Django 5.1 on 2024-08-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medlexicon', '0002_alter_worker_options_worker_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='date_added',
        ),
    ]
