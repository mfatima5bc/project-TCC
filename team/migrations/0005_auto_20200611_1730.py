# Generated by Django 3.0.5 on 2020-06-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_team_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='modify_date',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
    ]