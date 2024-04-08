# Generated by Django 3.2.25 on 2024-04-07 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DS', '0006_rename_years_project_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='harts',
            field=models.ManyToManyField(related_name='hart_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_project', to=settings.AUTH_USER_MODEL),
        ),
    ]
