# Generated by Django 5.2.2 on 2025-06-05 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genrer',
            new_name='genre',
        ),
    ]
