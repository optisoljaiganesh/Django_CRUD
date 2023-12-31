# Generated by Django 4.2.2 on 2023-06-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_categoriesimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
