# Generated by Django 4.2.3 on 2023-07-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]