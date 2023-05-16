# Generated by Django 4.1.5 on 2023-01-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]