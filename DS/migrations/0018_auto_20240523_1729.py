# Generated by Django 3.2.25 on 2024-05-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DS', '0017_auto_20240523_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imgfile',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='poster',
            field=models.FileField(upload_to='paperfile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repoter',
            field=models.FileField(upload_to='repoter/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='uploadedFile',
            field=models.FileField(upload_to='zipfile/'),
        ),
    ]
