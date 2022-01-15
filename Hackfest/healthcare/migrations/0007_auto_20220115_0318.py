# Generated by Django 3.2.8 on 2022-01-15 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0006_auto_20220114_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
