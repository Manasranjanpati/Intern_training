# Generated by Django 3.1 on 2021-04-01 06:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Formapp', '0002_enquirydata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirydata',
            name='cources',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('python', 'PYTHON'), ('django', 'Django'), ('java', 'JAVA'), ('node', 'NodeJs'), ('sql', 'SQL'), ('flutter', 'Flutter'), ('react', 'ReactJS')], max_length=200),
        ),
    ]
