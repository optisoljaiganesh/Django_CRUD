# Generated by Django 4.2.2 on 2023-06-19 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_categories_categoriesimg_categories_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriesimg',
            old_name='categories_img',
            new_name='categories',
        ),
    ]
