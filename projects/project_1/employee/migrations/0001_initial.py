# Generated by Django 3.1.7 on 2021-03-12 05:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('desription', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=150)),
                ('employee_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('employee_adress', models.TextField(blank=True, null=True)),
                ('employee_id', models.IntegerField()),
                ('employee_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.company')),
            ],
        ),
    ]
