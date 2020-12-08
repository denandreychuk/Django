# Generated by Django 3.1.4 on 2020-12-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApps', '0003_auto_20201207_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerapp',
            name='paid_status',
        ),
        migrations.AddField(
            model_name='customerapp',
            name='status',
            field=models.CharField(default='Test', max_length=20),
        ),
        migrations.AlterField(
            model_name='customerapp',
            name='token',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]