# Generated by Django 3.1.6 on 2021-04-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GFL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='lat',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='lon',
            field=models.IntegerField(blank=True),
        ),
    ]
