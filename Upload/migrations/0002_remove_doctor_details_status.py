# Generated by Django 5.0.3 on 2024-03-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_details',
            name='status',
        ),
    ]
