# Generated by Django 4.1.3 on 2022-11-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_todo_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='CreatedAt',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Due',
            field=models.DateField(blank=True, null=True),
        ),
    ]
