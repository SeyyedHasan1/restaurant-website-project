# Generated by Django 4.1 on 2022-08-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_rename_type_food_food_typefood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='typefood',
            new_name='type_food',
        ),
    ]
