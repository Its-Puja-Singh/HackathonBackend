# Generated by Django 3.2.8 on 2022-01-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0005_auto_20220114_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='insurancePlanName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='insurancePlanNumber',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
