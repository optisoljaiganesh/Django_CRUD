# Generated by Django 4.2.2 on 2023-06-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideamodel',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
