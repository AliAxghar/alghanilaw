# Generated by Django 2.2.6 on 2019-11-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics/')),
                ('title', models.CharField(max_length=100)),
                ('list2', models.CharField(max_length=100)),
                ('list3', models.CharField(max_length=100)),
                ('list4', models.CharField(max_length=100)),
                ('list5', models.CharField(max_length=100)),
                ('list6', models.CharField(max_length=100)),
                ('list7', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('civil law', 'CIVIL LAW'), ('criminal law', 'CRIMINAL LAW'), ('family law', 'FAMILY LAW'), ('writs', 'WRITS'), ('labour laws', 'LABOUR LAWS'), ('service matters', 'SERVICE MATTERS'), ('consumer matters', 'CONSUMER MATTERS'), ('immigrations', 'IMMIGRATIONS'), ('consultants', 'CONSULTANTS')], default='civil law', max_length=30)),
            ],
        ),
    ]
