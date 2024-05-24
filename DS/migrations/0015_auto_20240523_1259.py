# Generated by Django 3.2.25 on 2024-05-23 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DS', '0014_auto_20240516_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='poster',
            field=models.FileField(blank=True, null=True, upload_to='paperfile/'),
        ),
        migrations.AddField(
            model_name='project',
            name='repoter',
            field=models.FileField(blank=True, null=True, upload_to='repoter/'),
        ),
        migrations.CreateModel(
            name='OldProj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('member', models.CharField(max_length=100)),
                ('poster', models.FileField(blank=True, null=True, upload_to='paperfile/')),
                ('video', models.URLField()),
                ('repoter', models.FileField(blank=True, null=True, upload_to='repoter/')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DS.year')),
            ],
        ),
    ]
