# Generated by Django 3.2 on 2021-04-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrafterMall', '0012_remove_craft_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]