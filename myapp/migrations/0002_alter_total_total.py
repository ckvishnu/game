# Generated by Django 3.2.4 on 2021-09-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='total',
            field=models.CharField(max_length=20),
        ),
    ]
