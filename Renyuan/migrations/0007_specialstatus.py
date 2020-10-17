# Generated by Django 2.2 on 2020-08-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renyuan', '0006_auto_20200809_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='特殊身份')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='特殊身份代码')),
            ],
            options={
                'verbose_name': '特殊身份表',
                'verbose_name_plural': '特殊身份表',
                'db_table': '特殊身份表',
            },
        ),
    ]
