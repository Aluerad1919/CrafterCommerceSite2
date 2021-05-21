# Generated by Django 3.2 on 2021-05-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrafterMall', '0018_auto_20210418_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='digital_craft',
            name='material',
            field=models.CharField(default='Digital_Craft', max_length=45),
        ),
        migrations.AddField(
            model_name='jewelry_craft',
            name='material',
            field=models.CharField(default='Jewelry_Craft', max_length=45),
        ),
        migrations.AddField(
            model_name='leather_craft',
            name='material',
            field=models.CharField(default='Leather_Craft', max_length=45),
        ),
        migrations.AddField(
            model_name='metal_craft',
            name='material',
            field=models.CharField(default='Metal_Craft', max_length=45),
        ),
        migrations.AddField(
            model_name='textile_craft',
            name='material',
            field=models.CharField(default='Textile_Craft', max_length=45),
        ),
        migrations.AddField(
            model_name='wood_craft',
            name='material',
            field=models.CharField(default='Wood_Craft', max_length=45),
        ),
        migrations.AlterField(
            model_name='digital_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='jewelry_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='leather_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='metal_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='textile_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='wood_craft',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
