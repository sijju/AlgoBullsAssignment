# Generated by Django 4.1.3 on 2022-11-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_alter_todo_due'),
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
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
