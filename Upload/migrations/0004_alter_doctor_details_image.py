# Generated by Django 5.0.3 on 2024-03-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0003_alter_doctor_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_details',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
