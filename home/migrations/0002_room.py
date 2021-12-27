# Generated by Django 3.2.8 on 2021-12-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('QU', 'QUEEN'), ('DEL', 'DELUXE'), ('WAC', 'AC'), ('NAC', 'NON AC'), ('KIN', 'KING')], max_length=3)),
                ('bed', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
