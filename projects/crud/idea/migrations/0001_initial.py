# Generated by Django 4.2.2 on 2023-06-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.IntegerField(max_length=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
