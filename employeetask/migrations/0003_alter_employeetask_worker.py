# Generated by Django 5.0.3 on 2024-05-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeetask', '0002_alter_employeetask_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetask',
            name='worker',
            field=models.IntegerField(default=0),
        ),
    ]
