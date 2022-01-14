# Generated by Django 3.2.8 on 2022-01-14 04:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mobile', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter valid mobile number.', regex='^[6-9]\\d{9}$')])),
                ('email', models.EmailField(max_length=254)),
                ('registrationNumber', models.CharField(max_length=10)),
                ('bloodGroup', models.IntegerField(choices=[(1, 'A+'), (2, 'B+'), (3, 'O+'), (4, 'AB+'), (5, 'A-'), (6, 'B-'), (7, 'O-'), (8, 'AB-')], default=1)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('allergies', models.TextField(null=True)),
                ('symptoms', models.TextField(null=True)),
                ('pregnancyStatus', models.BooleanField(default=False)),
                ('previousSurgery', models.TextField(null=True)),
                ('isDiabetic', models.BooleanField(default=False)),
                ('insurancePlanName', models.CharField(blank=True, max_length=10)),
                ('status', models.IntegerField(choices=[(1, 'Recovered'), (2, 'Under Treatment')])),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
    ]