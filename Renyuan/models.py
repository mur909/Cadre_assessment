from django.db import models
from Bumen.models import Department
from Zhiwei.models import Rank

# Create your models here.
__all__ = ['Beiceping', 'Ceping']


class Beiceping(models.Model):
    """
    被测评人员信息表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=64, null=False, verbose_name='姓名')
    IDcard = models.CharField(max_length=64, null=False, unique=True, verbose_name='一卡通')
    # attribute = models.ForeignKey(to='Fangan.Attribute', default='', blank=True, null=True, related_name='ceping_attrubute', on_delete=models.CASCADE, verbose_name='单位属性')
    # label = models.TextField(default='', verbose_name='干部标签')
    post = models.CharField(max_length=64, null=False, verbose_name='岗位名称')
    post_id = models.CharField(max_length=12, null=False, unique=True, verbose_name='岗位代码')
    department = models.ForeignKey(to='Bumen.Department', to_field='department', related_name='Beiceping_department',
                                   null=False, on_delete=models.CASCADE,
                                   verbose_name='单位名称')
    department_num = models.ForeignKey(to='Bumen.Department', to_field='number',
                                       related_name='Beiceping_department_num',
                                       null=False, on_delete=models.CASCADE,
                                       verbose_name='单位代码')
    rank_id = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='Beiceping_number', null=False,
                                on_delete=models.CASCADE, verbose_name='职级代码')
    kaoHeZhe = models.CharField(max_length=64, null=False, verbose_name='考核的职级')
    department_type = models.CharField(max_length=12, null=False, verbose_name='单位性质')
    beiKaoHe = models.CharField(max_length=12, null=False, verbose_name='被考核角色')
    # EvaluationIndex = models.TextField(verbose_name='评价指标')
    cePing = models.BooleanField(default=False, verbose_name='是否参与测评')

    # 美化admin打印效果
    def __str__(self):
        return '{}--{}'.format(self.name, self.IDcard)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '被测评人员信息表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class Ceping(models.Model):
    """
    测评人员信息表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    department = models.ForeignKey(to='Bumen.Department', to_field='department', related_name='Ceping_department',
                                   null=False, on_delete=models.CASCADE,
                                   verbose_name='单位名称')
    name = models.CharField(max_length=64, null=False, verbose_name='姓名')
    IDcard = models.CharField(max_length=64, null=False, unique=True, verbose_name='一卡通')
    password = models.CharField(max_length=256, null=False, verbose_name='密码')
    # label = models.CharField(max_length=256, null=True, blank=True, verbose_name='测评身份标签')
    identityChoices = ((1, "机关"), (2, "学院"), (3, "直属单位"))
    identity = models.IntegerField(choices=identityChoices, null=False, verbose_name='身份')
    zhiwu = models.CharField(max_length=32, null=True, default='', verbose_name='职务')
    rank_id = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='Ceping_number', null=False,
                                on_delete=models.CASCADE, verbose_name='职级代码')
    post_id = models.ForeignKey(to='Renyuan.Beiceping', to_field='post_id', related_name='Ceping_post_id', null=True,
                                   on_delete=models.CASCADE, blank=True,  verbose_name='岗位代码')
    special_identity = models.CharField(max_length=64, blank=True, verbose_name='特殊人员身份')
    cePing = models.BooleanField(default=False, blank=True, verbose_name='是否参与测评')
    ganBu_finished = models.TextField(verbose_name='干部已测评')
    ganBu_unfinished = models.TextField(verbose_name='干部未测评')
    banZi_finished = models.TextField(verbose_name='领导班子已测评')
    banZi_unfinished = models.TextField(verbose_name='领导班子未测评')
    status = models.CharField(max_length=1, default='0', verbose_name='测评状态')
    # date = models.DateField(null=True, blank=True, verbose_name='出生日期')
    # job = models.CharField(max_length=32, null=True, blank=True, verbose_name='职称')
    # education = models.CharField(max_length=32, null=True, blank=True, verbose_name='学历')
    # political_status = models.CharField(max_length=32, null=True, blank=True, verbose_name='政治面貌')
    # mail = models.CharField(max_length=32, null=True, blank=True, verbose_name='邮箱')
    sessionid = models.CharField(max_length=32, null=True, verbose_name="当前是否已登录")

    # 美化admin打印效果
    def __str__(self):
        return ('{}--{}').format(self.name, self.IDcard)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '测评人员信息表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class SpecialStatus(models.Model):
    """
    特殊身份表
    """
    name = models.CharField(max_length=64, unique=True, verbose_name='特殊身份')
    code = models.CharField(max_length=32, unique=True, verbose_name='特殊身份代码')

    # 美化admin打印效果
    def __str__(self):
        return '{}--{}'.format(self.name, self.code)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '特殊身份表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class Zhiwu(models.Model):
    """
    职务表
    """
    name = models.CharField(max_length=64, unique=True, verbose_name='职务名')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '职务表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name
