# Generated by Django 2.2 on 2020-08-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0004_auto_20200806_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='角色名称'),
        ),
    ]