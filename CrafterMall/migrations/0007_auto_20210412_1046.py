# Generated by Django 3.2 on 2021-04-12 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrafterMall', '0006_auto_20210411_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craft',
            old_name='user_craft',
            new_name='seller',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
