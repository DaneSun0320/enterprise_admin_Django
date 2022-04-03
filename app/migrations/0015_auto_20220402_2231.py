# Generated by Django 2.2.5 on 2022-04-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220401_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskRegion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('riskLevel', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='outsideinfo',
            old_name='region',
            new_name='district',
        ),
    ]
