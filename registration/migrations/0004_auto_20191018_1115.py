# Generated by Django 2.2.6 on 2019-10-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20191018_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number_phone',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
