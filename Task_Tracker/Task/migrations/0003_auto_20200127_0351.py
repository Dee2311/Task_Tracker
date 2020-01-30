# Generated by Django 3.0.2 on 2020-01-26 22:21

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_auto_20200127_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
        migrations.AddField(
            model_name='tasklist',
            name='sub_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Task.TaskList'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='description',
            field=models.TextField(verbose_name=builtins.max),
        ),
    ]
