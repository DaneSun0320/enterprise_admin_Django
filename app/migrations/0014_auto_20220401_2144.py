# Generated by Django 2.2.5 on 2022-04-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220331_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='uid',
            field=models.CharField(max_length=80),
        ),
    ]