# Generated by Django 2.2.6 on 2019-11-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20191108_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='location',
            field=models.CharField(default='lahore,pakistan', max_length=50),
        ),
    ]