# Generated by Django 3.0.2 on 2020-01-26 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20200127_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
