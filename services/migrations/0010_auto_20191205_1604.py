# Generated by Django 2.2.6 on 2019-12-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_remove_service_list5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='list1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='list2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='list3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='list4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.TextField(),
        ),
    ]
