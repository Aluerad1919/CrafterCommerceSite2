# Generated by Django 3.1.5 on 2021-04-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrafterMall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]
