# Generated by Django 4.2.2 on 2023-06-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_employeedetails_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
