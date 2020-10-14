# Generated by Django 2.2 on 2020-09-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renyuan', '0012_auto_20200907_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zhiwu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='职务名')),
            ],
            options={
                'verbose_name': '职务表',
                'verbose_name_plural': '职务表',
                'db_table': '职务表',
            },
        ),
        migrations.AlterField(
            model_name='ceping',
            name='zhiwu',
            field=models.CharField(default='', max_length=32, null=True, verbose_name='职务'),
        ),
    ]