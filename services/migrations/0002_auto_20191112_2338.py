# Generated by Django 2.2.6 on 2019-11-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='list2',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='list3',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='list4',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='list5',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='list6',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='list7',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
