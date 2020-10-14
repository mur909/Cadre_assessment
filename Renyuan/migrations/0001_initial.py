# Generated by Django 2.2 on 2020-08-02 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bumen', '0001_initial'),
        ('Zhiwei', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beiceping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('IDcard', models.CharField(max_length=64, unique=True, verbose_name='一卡通')),
                ('post', models.CharField(max_length=64, verbose_name='岗位名称')),
                ('post_id', models.CharField(max_length=12, unique=True, verbose_name='岗位代码')),
                ('kaoHeZhe', models.CharField(max_length=64, verbose_name='考核的职级')),
                ('department_type', models.CharField(max_length=12, verbose_name='单位性质')),
                ('beiKaoHe', models.CharField(max_length=12, verbose_name='被考核角色')),
                ('EvaluationIndex', models.TextField(verbose_name='评价指标')),
                ('cePing', models.BooleanField(default=False, verbose_name='是否参与测评')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beiceping_department', to='Bumen.Department', to_field='department', verbose_name='单位名称')),
                ('department_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beiceping_department_num', to='Bumen.Department', to_field='number', verbose_name='单位代码')),
                ('rank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beiceping_number', to='Zhiwei.Rank', to_field='number', verbose_name='职级代码')),
            ],
            options={
                'verbose_name': '被测评人员信息表',
                'verbose_name_plural': '被测评人员信息表',
                'db_table': '被测评人员信息表',
            },
        ),
        migrations.CreateModel(
            name='Ceping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('IDcard', models.CharField(max_length=64, unique=True, verbose_name='一卡通')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('identity', models.IntegerField(choices=[(1, '机关'), (2, '学院'), (3, '直属单位')], verbose_name='身份')),
                ('zhiwu', models.CharField(default='', max_length=32, verbose_name='职务')),
                ('special_identity', models.CharField(blank=True, max_length=64, verbose_name='特殊人员身份')),
                ('cePing', models.BooleanField(blank=True, default=False, verbose_name='是否参与测评')),
                ('ganBu_finished', models.TextField(default='', verbose_name='干部已测评')),
                ('ganBu_unfinished', models.TextField(default='', verbose_name='干部未测评')),
                ('banZi_finished', models.TextField(default='', verbose_name='领导班子已测评')),
                ('banZi_unfinished', models.TextField(default='', verbose_name='领导班子未测评')),
                ('status', models.CharField(default='0', max_length=1, verbose_name='测评状态')),
                ('date', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('job', models.CharField(blank=True, max_length=32, null=True, verbose_name='职称')),
                ('education', models.CharField(blank=True, max_length=32, null=True, verbose_name='学历')),
                ('political_status', models.CharField(blank=True, max_length=32, null=True, verbose_name='政治面貌')),
                ('mail', models.CharField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ceping_department', to='Bumen.Department', to_field='department', verbose_name='单位名称')),
                ('post_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ceping_post_id', to='Renyuan.Beiceping', to_field='post_id', verbose_name='岗位代码')),
                ('rank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ceping_number', to='Zhiwei.Rank', to_field='number', verbose_name='职级代码')),
            ],
            options={
                'verbose_name': '测评人员信息表',
                'verbose_name_plural': '测评人员信息表',
                'db_table': '测评人员信息表',
            },
        ),
    ]