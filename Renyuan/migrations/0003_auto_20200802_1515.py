# Generated by Django 2.2 on 2020-08-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renyuan', '0002_auto_20200802_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beiceping',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='ceping',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
    ]
