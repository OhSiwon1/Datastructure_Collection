# Generated by Django 3.2.25 on 2024-04-04 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DS', '0004_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='years',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DS.year'),
            preserve_default=False,
        ),
    ]
