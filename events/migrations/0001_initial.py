# Generated by Django 5.1.6 on 2025-02-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('organizer', models.CharField(max_length=100)),
            ],
        ),
    ]
