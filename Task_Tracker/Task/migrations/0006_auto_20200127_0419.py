# Generated by Django 3.0.2 on 2020-01-26 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0005_auto_20200127_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='sub_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Task.TaskList'),
        ),
    ]
