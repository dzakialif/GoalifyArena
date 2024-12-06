# Generated by Django 5.1.3 on 2024-12-05 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.TextField()),
                ('field_image', models.ImageField(blank=True, null=True, upload_to='field/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('session', models.CharField(choices=[('session1', '08:00 - 10:00'), ('session2', '10:00 - 12:00'), ('session3', '12:00 - 14:00'), ('session4', '14:00 - 16:00'), ('session5', '16:00 - 18:00'), ('session6', '18:00 - 20:00'), ('session7', '20:00 - 22:00')], max_length=20)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], default='Available', max_length=10)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='arena.field')),
            ],
            options={
                'ordering': ['date', 'session'],
                'unique_together': {('field', 'date', 'session')},
            },
        ),
    ]
