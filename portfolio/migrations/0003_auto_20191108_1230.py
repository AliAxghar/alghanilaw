# Generated by Django 2.2.6 on 2019-11-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_updated_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='created_on',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]