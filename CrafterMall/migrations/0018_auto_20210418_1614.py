# Generated by Django 3.2 on 2021-04-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrafterMall', '0017_delete_craft'),
    ]

    operations = [
        migrations.AddField(
            model_name='digital_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='digital_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='digital_craft',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jewelry_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='jewelry_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='jewelry_craft',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leather_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='leather_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='leather_craft',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metal_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='metal_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='metal_craft',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textile_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='textile_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='textile_craft',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wood_craft',
            name='craft_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='wood_craft',
            name='craft_name',
            field=models.CharField(default=' ', max_length=45),
        ),
        migrations.AddField(
            model_name='wood_craft',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]