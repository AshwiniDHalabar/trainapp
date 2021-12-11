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