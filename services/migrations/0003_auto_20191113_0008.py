# Generated by Django 2.2.6 on 2019-11-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20191112_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='list1',
            field=models.CharField(default='Criminal law, the body of law that defines criminal offenses, regulates the apprehension.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='list2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='list3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='list4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='list5',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='list6',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='list7',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]