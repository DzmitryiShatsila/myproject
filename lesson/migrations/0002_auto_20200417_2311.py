# Generated by Django 3.0.5 on 2020-04-17 20:11

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='material',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
