# Generated by Django 5.0 on 2024-03-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='starting_price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
