from django.db import models


# Create your models here.


class Department(models.Model):
    """
    单位表
    """
    id = models.AutoField(primary_key=True, verbose_name='序号')
    department = models.CharField(max_length=64, null=False, unique=True, verbose_name='单位')
    number = models.CharField(max_length=12, null=False, unique=True, verbose_name='单位代码')
    category = models.CharField(max_length=12, null=False, verbose_name='类别')

    # 美化打印效果
    def __str__(self):
        return self.department

    class Meta:
        # 在admin中显示中文表名
        verbose_name = '单位表'
        db_table = verbose_name
        # 去掉s
        verbose_name_plural = verbose_name
