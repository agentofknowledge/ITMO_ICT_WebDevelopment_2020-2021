# Generated by Django 3.1.3 on 2020-11-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20201114_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]
