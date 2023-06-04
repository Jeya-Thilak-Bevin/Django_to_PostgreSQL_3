# Generated by Django 4.2 on 2023-05-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('price', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
