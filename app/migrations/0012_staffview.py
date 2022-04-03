# Generated by Django 2.2.5 on 2022-03-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220329_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffView',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.BigIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('sex', models.BooleanField()),
                ('age', models.SmallIntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('sector', models.IntegerField()),
                ('sectorName', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
            ],
            options={
                'db_table': 'staffview',
                'managed': False,
            },
        ),
    ]
