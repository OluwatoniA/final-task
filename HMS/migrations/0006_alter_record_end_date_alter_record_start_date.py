# Generated by Django 4.0.5 on 2022-06-16 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0005_rename_hotel_records_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='end_date',
            field=models.DateField(verbose_name='%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='record',
            name='start_date',
            field=models.DateField(verbose_name='%Y-%m-%d'),
        ),
    ]