from django.db import models


# Create your models here.


class Position(models.Model):
    """
    职位表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    position = models.CharField(max_length=12, null=False, unique=True, verbose_name='职位')
    number = models.CharField(max_length=12, null=False, unique=True, verbose_name='职位代码')

    # 美化打印效果
    def __str__(self):
        return self.position

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '职位表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name


class Rank(models.Model):
    """
    职级表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    rank = models.CharField(max_length=12, null=False, unique=True, verbose_name='职级')
    number = models.CharField(max_length=12, null=False, unique=True, verbose_name='职级代码')

    # 美化admin打印效果
    def __str__(self):
        return self.number

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '职级表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name
