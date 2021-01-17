# Generated by Django 3.0.5 on 2021-01-17 00:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0007_auto_20201021_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('initDate', models.DateField(auto_now_add=True)),
                ('endDate', models.DateField()),
                ('order', models.IntegerField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toDo', to='team.Team')),
            ],
            options={
                'index_together': {('group', 'order')},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=800)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('priority', models.CharField(max_length=10)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('toDo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='project.ToDo')),
            ],
            options={
                'index_together': {('toDo', 'order')},
            },
        ),
    ]
