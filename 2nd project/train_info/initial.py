# Generated by Django 3.2.9 on 2021-12-08 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('duration', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'train',
            },
        ),
    ]
