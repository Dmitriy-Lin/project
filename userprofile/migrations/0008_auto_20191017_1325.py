# Generated by Django 2.2.6 on 2019-10-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20191017_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.FileField(upload_to='img/'),
        ),
    ]
