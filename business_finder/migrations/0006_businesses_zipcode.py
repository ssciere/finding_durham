# Generated by Django 2.1 on 2019-06-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_finder', '0005_auto_20190604_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesses',
            name='zipCode',
            field=models.CharField(default=0, max_length=20),
        ),
    ]