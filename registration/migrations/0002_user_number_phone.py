# Generated by Django 2.2.5 on 2019-09-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_phone',
            field=models.CharField(max_length=256, null=True),
        ),
    ]