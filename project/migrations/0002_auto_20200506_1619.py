# Generated by Django 3.0.5 on 2020-05-06 19:19

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StepManager',
        ),
        migrations.AlterModelManagers(
            name='task',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
