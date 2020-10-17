from django.db import models


# Create your models here.
class Gbresult(models.Model):
    """
    干部考核结果汇总表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=64, null=False, verbose_name='姓名')
    IDcard = models.CharField(max_length=64, null=False, verbose_name='一卡通')
    department = models.CharField(max_length=64, null=False, verbose_name='单位名称')
    category = models.CharField(max_length=16, null=False, verbose_name='单位类别')
    beiKaoHe = models.CharField(max_length=16, null=False, verbose_name='职称标识')
    year = models.CharField(max_length=4, null=False, verbose_name='年份')
    index1 = models.DecimalField(max_digits=7, decimal_places=4)
    index2 = models.DecimalField(max_digits=7, decimal_places=4)
    index3 = models.DecimalField(max_digits=7, decimal_places=4)
    index4 = models.DecimalField(max_digits=7, decimal_places=4)
    index5 = models.DecimalField(max_digits=7, decimal_places=4)
    index6 = models.DecimalField(max_digits=7, decimal_places=4)
    index7 = models.DecimalField(max_digits=7, decimal_places=4)
    index8 = models.DecimalField(max_digits=7, decimal_places=4)
    index9 = models.DecimalField(max_digits=7, decimal_places=4)
    index10 = models.DecimalField(max_digits=7, decimal_places=4)
    index11 = models.DecimalField(max_digits=7, decimal_places=4)
    index12 = models.DecimalField(max_digits=7, decimal_places=4)
    index13 = models.DecimalField(max_digits=7, decimal_places=4)
    index14 = models.DecimalField(max_digits=7, decimal_places=4)
    index15 = models.DecimalField(max_digits=7, decimal_places=4)
    index16 = models.DecimalField(max_digits=7, decimal_places=4)
    index17 = models.DecimalField(max_digits=7, decimal_places=4)
    index18 = models.DecimalField(max_digits=7, decimal_places=4)
    index19 = models.DecimalField(max_digits=7, decimal_places=4)
    index20 = models.DecimalField(max_digits=7, decimal_places=4)
    index21 = models.DecimalField(max_digits=7, decimal_places=4)
    index22 = models.DecimalField(max_digits=7, decimal_places=4)
    index23 = models.DecimalField(max_digits=7, null=True, decimal_places=4)
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评总分')
    rankingOfLine = models.SmallIntegerField(null=True, verbose_name='条线内排名')
    rankingOfDep = models.SmallIntegerField(null=True, verbose_name='本单位排名')
    rankingofCategory = models.SmallIntegerField(null=True, verbose_name='机关or学院or直属单位排名')
    rankingOfAll = models.SmallIntegerField(null=True, verbose_name='综合排名')
    TopTen = models.BooleanField(null=True, verbose_name='前百分之十')
    LastTen = models.BooleanField(null=True, verbose_name='后百分之十')
    Excellent = models.BooleanField(null=True, verbose_name='优秀')

    def __str__(self):
        return self.name

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '干部考核结果汇总表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class Bzresult(models.Model):
    """
    班子考核结果汇总表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    beiceping = models.CharField(max_length=64, null=False, verbose_name='单位')
    year = models.CharField(max_length=4, null=False, verbose_name='年份')
    index1 = models.DecimalField(max_digits=7, decimal_places=4)
    index2 = models.DecimalField(max_digits=7, decimal_places=4)
    index3 = models.DecimalField(max_digits=7, decimal_places=4)
    index4 = models.DecimalField(max_digits=7, decimal_places=4)
    index5 = models.DecimalField(max_digits=7, decimal_places=4)
    index6 = models.DecimalField(max_digits=7, decimal_places=4)
    index7 = models.DecimalField(max_digits=7, decimal_places=4)
    index8 = models.DecimalField(max_digits=7, decimal_places=4)
    index9 = models.DecimalField(max_digits=7, decimal_places=4)
    index10 = models.DecimalField(max_digits=7, decimal_places=4)
    index11 = models.DecimalField(max_digits=7, decimal_places=4)
    index12 = models.DecimalField(max_digits=7, decimal_places=4)
    index19 = models.DecimalField(max_digits=7, null=True, decimal_places=4)
    index20 = models.DecimalField(max_digits=7, null=True, decimal_places=4)
    index21 = models.DecimalField(max_digits=7, null=True, decimal_places=4)
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评总分')
    rankingOfLine = models.CharField(max_length=5, null=True, verbose_name='条线内排名')
    rankingOfAll = models.CharField(max_length=5, null=True, verbose_name='综合排名')
    TopTen = models.BooleanField(null=True, verbose_name='前百分之十')
    LastTen = models.BooleanField(null=True, verbose_name='后百分之十')
    Excellent = models.BooleanField(null=True, verbose_name='优秀')

    def __str__(self):
        return self.beiceping

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '班子考核结果汇总表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name