# Generated by Django 4.1.3 on 2022-11-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('WORKING', 'WORKING'), ('OVERDUE', 'OVERDUE'), ('COMPLETED', 'COMPLETED')], default='OPEN', max_length=10),
        ),
    ]
