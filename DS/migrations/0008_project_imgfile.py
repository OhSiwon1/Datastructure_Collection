# Generated by Django 3.2.25 on 2024-04-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DS', '0007_auto_20240407_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]