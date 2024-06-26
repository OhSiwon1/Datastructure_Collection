# Generated by Django 3.2.25 on 2024-05-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DS', '0012_alter_project_abstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='hashtag',
            field=models.ManyToManyField(related_name='project_hashtag', to='DS.Hashtag'),
        ),
    ]
