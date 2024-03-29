# Generated by Django 2.1 on 2019-06-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_finder', '0003_businesses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='category',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='phoneNumber',
            field=models.CharField(max_length=50),
        ),
    ]
