# Generated by Django 4.1.3 on 2022-11-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_alter_todo_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
