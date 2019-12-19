# Generated by Django 2.2.6 on 2019-11-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics/')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=50)),
                ('para1', models.TextField()),
                ('para2', models.TextField()),
                ('para3', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('civil law', 'CIVIL LAW'), ('criminal law', 'CRIMINAL LAW'), ('family law', 'FAMILY LAW'), ('writs', 'WRITS'), ('labour laws', 'LABOUR LAWS'), ('service matters', 'SERVICE MATTERS'), ('consumer matters', 'CONSUMER MATTERS'), ('immigrations', 'IMMIGRATIONS'), ('consultants', 'CONSULTANTS')], default='civil law', max_length=20)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
    ]