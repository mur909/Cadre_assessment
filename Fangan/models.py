from django.db import models
from Bumen.models import Department
from Zhiwei.models import Rank
# from Renyuan.models import Beiceping, Ceping

__all__ = ['EvaluationItem', 'GbCpWeight', 'GbPjIndex', 'jggbIndexWeight', 'jggbTongji', 'jggbResult', 'xygbIndexWeight', 'xygbTongji',
           'xygbResult', 'zsdwgbIndexWeight', 'zsdwgbTongji', 'zsdwgbResult', 'BzCpWeight', 'BzPjIndex', 'BzTjInfo',
           'xybzIndexWeight', 'xybzTongji', 'xybzResult', 'zsdwbzIndexWeight', 'zsdwbzTongji', 'zsdwbzResult']


# Create your models here.
class EvaluationItem(models.Model):
    """
    测评项表
    """
    item = models.CharField(max_length=12, null=False, unique=True, verbose_name="测评项")
    code = models.CharField(max_length=12, null=False, unique=True, verbose_name="代码")
    score = models.CharField(max_length=12, null=False, unique=True, verbose_name="分值")

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '测评项表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class GbCpWeight(models.Model):
    """
    干部测评权重表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=32, null=True, verbose_name='名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=3, null=True, decimal_places=2, verbose_name='权重')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '干部测评权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class GbPjIndex(models.Model):
    """
    干部评价指标表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    index = models.CharField(max_length=12, null=True, verbose_name='评价指标')
    code = models.CharField(max_length=12, null=True, unique=True, verbose_name='指标代码')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '干部评价指标表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class jggbIndexWeight(models.Model):
    """机关干部指标权重表"""
    index = models.CharField(max_length=12, null=True, verbose_name='指标名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=4, null=True, decimal_places=3, verbose_name='权重')

    def __str__(self):
        return '{}-{}-{}'.format(self.index, self.code, self.weight)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '机关干部指标权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class jggbTongji(models.Model):
    """机关干部统计表"""
    ceping = models.ForeignKey(to='Renyuan.Ceping', to_field='IDcard', related_name='jggbceping',
                               on_delete=models.CASCADE,
                               verbose_name='测评人')
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='jggbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标1')
    index2 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标2')
    index3 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标3')
    index4 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标4')
    index5 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标5')
    index6 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标6')
    index7 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标7')
    index8 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标8')
    index9 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标9')
    index10 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标10')
    index11 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标11')
    index12 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标12')
    index13 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标13')
    index14 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标14')
    index15 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标15')
    index16 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标16')
    index17 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标17')
    index18 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标18')
    rankNum = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='jggbzhijidaima',
                                on_delete=models.CASCADE,
                                verbose_name='职级代码')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='jggbdanweidaima',
                               on_delete=models.CASCADE,
                               verbose_name='单位代码')
    giveup = models.BooleanField(default=False, verbose_name='放弃测评')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '机关干部统计表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class jggbResult(models.Model):
    """机关干部结果表"""
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='re_jggbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标1')
    index2 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标2')
    index3 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标3')
    index4 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标4')
    index5 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标5')
    index6 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标6')
    index7 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标7')
    index8 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标8')
    index9 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标9')
    index10 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标10')
    index11 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标11')
    index12 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标12')
    index13 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标13')
    index14 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标14')
    index15 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标15')
    index16 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标16')
    index17 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标17')
    index18 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标18')
    level = models.CharField(max_length=12, verbose_name='级别')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='jggbdanwei',
                               on_delete=models.CASCADE,
                               verbose_name='单位')
    zhiwu = models.CharField(max_length=12, verbose_name='职务')
    count = models.CharField(max_length=5, verbose_name='测评人数')
    index19 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标19')
    index20 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标20')
    index21 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标21')
    index22 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标22')
    index23 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标23')
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评分数')

    def __str__(self):
        return '{}-{}'.format(self.beiceping_id, self.get_level_display())

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '机关干部结果表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xygbIndexWeight(models.Model):
    """学院干部指标权重表"""
    index = models.CharField(max_length=12, null=True, verbose_name='指标名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=4, null=True, decimal_places=3, verbose_name='权重')

    def __str__(self):
        return '{}-{}-{}'.format(self.index, self.code, self.weight)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院干部指标权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xygbTongji(models.Model):
    """学院干部统计表"""
    ceping = models.ForeignKey(to='Renyuan.Ceping', to_field='IDcard', related_name='xygbceping',
                               on_delete=models.CASCADE,
                               verbose_name='测评人')
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='xygbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标1')
    index2 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标2')
    index3 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标3')
    index4 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标4')
    index5 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标5')
    index6 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标6')
    index7 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标7')
    index8 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标8')
    index9 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标9')
    index10 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标10')
    index11 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标11')
    index12 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标12')
    index13 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标13')
    index14 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标14')
    index15 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标15')
    index16 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标16')
    index17 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标17')
    index18 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标18')
    rankNum = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='xygbzhijidaima',
                                on_delete=models.CASCADE,
                                verbose_name='职级代码')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='xygbdanweidaima',
                               on_delete=models.CASCADE,
                               verbose_name='单位代码')
    giveup = models.BooleanField(default=False, verbose_name='放弃测评')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院干部统计表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xygbResult(models.Model):
    """学院干部结果表"""
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='re_xygbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标1')
    index2 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标2')
    index3 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标3')
    index4 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标4')
    index5 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标5')
    index6 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标6')
    index7 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标7')
    index8 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标8')
    index9 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标9')
    index10 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标10')
    index11 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标11')
    index12 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标12')
    index13 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标13')
    index14 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标14')
    index15 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标15')
    index16 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标16')
    index17 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标17')
    index18 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标18')
    level = models.CharField(max_length=12, verbose_name='级别')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='xygbdanwei',
                               on_delete=models.CASCADE,
                               verbose_name='单位')
    zhiwu = models.CharField(max_length=12, blank=True, verbose_name='职务')
    count = models.CharField(max_length=5, verbose_name='测评人数')
    index19 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标19')  # 学院校领导
    index20 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标20')  # 班子成员
    index21 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标21')  # 学院师生
    index22 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标22')  # 对口机关
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评分数')

    def __str__(self):
        return self.beiceping_id

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院干部结果表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwgbIndexWeight(models.Model):
    """直属单位干部指标权重表"""
    index = models.CharField(max_length=12, null=True, verbose_name='指标名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=4, null=True, decimal_places=3, verbose_name='权重')

    def __str__(self):
        return '{}-{}-{}'.format(self.index, self.code, self.weight)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位干部指标权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwgbTongji(models.Model):
    """直属单位干部统计表"""
    ceping = models.ForeignKey(to='Renyuan.Ceping', to_field='IDcard', related_name='zsdwgbceping',
                               on_delete=models.CASCADE,
                               verbose_name='测评人')
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='zsdwgbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标1')
    index2 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标2')
    index3 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标3')
    index4 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标4')
    index5 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标5')
    index6 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标6')
    index7 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标7')
    index8 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标8')
    index9 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标9')
    index10 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标10')
    index11 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标11')
    index12 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标12')
    index13 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标13')
    index14 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标14')
    index15 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标15')
    index16 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标16')
    index17 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标17')
    index18 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标18')
    rankNum = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='zsdwgbzhijidaima',
                                on_delete=models.CASCADE,
                                verbose_name='职级代码')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='zsdwgbdanweidaima',
                               on_delete=models.CASCADE,
                               verbose_name='单位代码')
    giveup = models.BooleanField(default=False, verbose_name='放弃测评')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位干部统计表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwgbResult(models.Model):
    """直属单位干部结果表"""
    beiceping = models.ForeignKey(to='Renyuan.Beiceping', to_field='IDcard', related_name='re_zsdwgbbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评人')
    index1 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标1')
    index2 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标2')
    index3 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标3')
    index4 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标4')
    index5 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标5')
    index6 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标6')
    index7 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标7')
    index8 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标8')
    index9 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标9')
    index10 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标10')
    index11 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标11')
    index12 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标12')
    index13 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标13')
    index14 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标14')
    index15 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标15')
    index16 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标16')
    index17 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标17')
    index18 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标18')
    level = models.CharField(max_length=12, verbose_name='级别')
    depNum = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='zsdwgbdanwei',
                               on_delete=models.CASCADE,
                               verbose_name='单位')
    zhiwu = models.CharField(max_length=12, verbose_name='职务')
    count = models.CharField(max_length=5, verbose_name='测评人数')
    index19 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标19')  # 直属单位校领导
    index20 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标20')  # 单位班子
    index21 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标21')  # 相关人员
    index22 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标22')  # 直属单位学院领导
    index23 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标23')  # 直属单位学院相关
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评分数')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位干部结果表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class BzCpWeight(models.Model):
    """
    领导班子测评权重表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=32, null=True, verbose_name='名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=3, null=True, decimal_places=2, verbose_name='权重')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '领导班子测评权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class BzPjIndex(models.Model):
    """
    领导班子评价指标表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    index = models.CharField(max_length=12, null=True, verbose_name='评价指标')
    code = models.CharField(max_length=12, null=True, unique=True, verbose_name='指标代码')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '领导班子评价指标表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class BzTjInfo(models.Model):
    """
    领导班子统计信息表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    department = models.OneToOneField(to='Bumen.Department', to_field='department', related_name='BzTjInfo_department',
                                      on_delete=models.CASCADE,
                                      verbose_name='单位名称')
    number = models.OneToOneField(to='Bumen.Department', to_field='number', related_name='BzTjInfo_number', null=False,
                                  on_delete=models.CASCADE,
                                  verbose_name='单位代码')
    # label = models.TextField(default='', verbose_name='班子标签')
    type = models.CharField(max_length=12, null=False, verbose_name='性质')
    # evaluation_index = models.CharField(max_length=256, verbose_name='评价指标')
    cePing = models.BooleanField(default=True, verbose_name='测评')  # 没什么作用，没写对应的功能

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '领导班子统计信息表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xybzIndexWeight(models.Model):
    """学院班子指标权重表"""
    index = models.CharField(max_length=12, null=True, verbose_name='指标名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=4, null=True, decimal_places=3, verbose_name='权重')

    def __str__(self):
        return '{}-{}-{}'.format(self.index, self.code, self.weight)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院班子指标权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xybzTongji(models.Model):
    """学院班子统计表"""
    ceping = models.ForeignKey(to='Renyuan.Ceping', to_field='IDcard', related_name='xybzceping',
                               on_delete=models.CASCADE,
                               verbose_name='测评人')
    beiceping = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='xybzbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评单位')
    index1 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标1')
    index2 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标2')
    index3 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标3')
    index4 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标4')
    index5 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标5')
    index6 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标6')
    index7 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标7')
    index8 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标8')
    index9 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标9')
    index10 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标10')
    index11 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标11')
    index12 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标12')
    depcode = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='xybzdanweidaima',
                                on_delete=models.CASCADE,
                                verbose_name='单位代码')
    rankNum = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='xybzzhijidaima',
                                on_delete=models.CASCADE,
                                verbose_name='职级代码')
    giveup = models.BooleanField(default=False, verbose_name='放弃测评')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院班子统计表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class xybzResult(models.Model):
    """学院班子结果表"""
    beiceping = models.OneToOneField(to='Bumen.Department', to_field='number', related_name='xybzresult',
                                     on_delete=models.CASCADE,
                                     verbose_name='单位')
    index1 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标1')
    index2 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标2')
    index3 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标3')
    index4 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标4')
    index5 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标5')
    index6 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标6')
    index7 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标7')
    index8 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标8')
    index9 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标9')
    index10 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标10')
    index11 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标11')
    index12 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标12')
    count = models.CharField(max_length=5, verbose_name='测评人数')
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评分数')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '学院班子结果表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwbzIndexWeight(models.Model):
    """直属单位班子指标权重表"""
    index = models.CharField(max_length=12, null=True, verbose_name='指标名称')
    code = models.CharField(max_length=12, verbose_name='指标代码')
    weight = models.DecimalField(max_digits=4, null=True, decimal_places=3, verbose_name='权重')

    def __str__(self):
        return '{}-{}-{}'.format(self.index, self.code, self.weight)

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位班子指标权重表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwbzTongji(models.Model):
    """直属单位班子统计表"""
    ceping = models.ForeignKey(to='Renyuan.Ceping', to_field='IDcard', related_name='zsdwbzceping',
                               on_delete=models.CASCADE,
                               verbose_name='测评人')
    beiceping = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='zsdwbzbeiceping',
                                  on_delete=models.CASCADE,
                                  verbose_name='被测评单位')
    index1 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标1')
    index2 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标2')
    index3 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标3')
    index4 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标4')
    index5 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标5')
    index6 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标6')
    index7 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标7')
    index8 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标8')
    index9 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标9')
    index10 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标10')
    index11 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标11')
    index12 = models.SmallIntegerField(null=True, blank=True, verbose_name='指标12')
    depcode = models.ForeignKey(to='Bumen.Department', to_field='number', related_name='zsdwbzdanweidaima',
                                on_delete=models.CASCADE,
                                verbose_name='单位代码')
    rankNum = models.ForeignKey(to='Zhiwei.Rank', to_field='number', related_name='zsdwbzzhijidaima',
                                on_delete=models.CASCADE,
                                verbose_name='职级代码')
    giveup = models.BooleanField(default=False, verbose_name='放弃测评')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位班子统计表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class zsdwbzResult(models.Model):
    """直属单位班子结果表"""
    beiceping = models.OneToOneField(to='Bumen.Department', to_field='number', related_name='zsdwbzresult',
                                     on_delete=models.CASCADE,
                                     verbose_name='单位')
    index1 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标1')
    index2 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标2')
    index3 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标3')
    index4 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标4')
    index5 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标5')
    index6 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标6')
    index7 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标7')
    index8 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标8')
    index9 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标9')
    index10 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标10')
    index11 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标11')
    index12 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标12')
    count = models.CharField(max_length=5, verbose_name='测评人数')
    index19 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标19')  # 校领导
    index20 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标20')  # 党政负责人
    index21 = models.DecimalField(max_digits=7, null=True, blank=True, decimal_places=4, verbose_name='指标21')  # 单位职工师生代表
    score = models.DecimalField(max_digits=15, decimal_places=12, verbose_name='测评分数')

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '直属单位班子结果表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


# class Attribute(models.Model):
#     """
#     属性表
#     """
#     name = models.CharField(max_length=12, verbose_name='名称')
#     code = models.CharField(max_length=12, verbose_name='代码')
#
#     class Meta:
#         # 在admin中显示中文表名
#         verbose_name = '属性表'
#         db_table = verbose_name
#         # 去掉s
#         verbose_name_plural = verbose_name


# class CepingLabel(models.Model):
#     """
#     参评身份
#     """
#     label = models.CharField(max_length=256, verbose_name='参评身份')
#     code = models.CharField(max_length=12, unique=True, verbose_name='代码')
#     category = models.CharField(max_length=12, verbose_name='分类')
#
#     class Meta:
#         # 在admin中显示中文表名
#         verbose_name = '参评身份'
#         db_table = verbose_name
#         # 去掉s
#         verbose_name_plural = verbose_name


# class GanbuLabel(models.Model):
#     """
#     被考核干部身份表
#     """
#     label = models.CharField(max_length=256, verbose_name='被考核干部')
#     code = models.CharField(max_length=12, unique=True, verbose_name='代码')
#     category = models.CharField(max_length=12, verbose_name='分类')
#
#     class Meta:
#         # 在admin中显示中文表名
#         verbose_name = '被考核干部身份表'
#         db_table = verbose_name
#         # 去掉s
#         verbose_name_plural = verbose_name


# class BanziLabel(models.Model):
#     """
#     被考核班子身份表
#     """
#     label = models.CharField(max_length=256, verbose_name='被考核班子')
#     code = models.CharField(max_length=12, unique=True, verbose_name='代码')
#     category = models.CharField(max_length=12, verbose_name='分类')
#
#     class Meta:
#         # 在admin中显示中文表名
#         verbose_name = '被考核班子身份表'
#         db_table = verbose_name
#         # 去掉s
#         verbose_name_plural = verbose_name


# class Relationship (models.Model):
#     """
#     考核关系对应表
#     """
#     ceping_code = models.CharField(max_length=12, verbose_name='参评代码')
#     ganbu_code = models.TextField(verbose_name='被考核干部代码')
#     banzi_code = models.TextField(verbose_name='被考核班子代码')
#
#     class Meta:
#         # 在admin中显示中文表名
#         verbose_name = '考核关系对应表'
#         db_table = verbose_name
#         # 去掉s
#         verbose_name_plural = verbose_name