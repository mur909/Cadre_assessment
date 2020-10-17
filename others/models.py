from django.db import models
from Bumen.models import Department
import hashlib


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32, null=False, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, null=False, verbose_name='密码')
    token = models.UUIDField(null=True, blank=True)
    create_token_time = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(to='Bumen.Department', to_field='number', null=True, blank=True,
                                   on_delete=models.CASCADE, verbose_name='单位')
    # roles = models.ManyToManyField(to='Role', verbose_name='用户所拥有的角色', blank=True)
    roles = models.ForeignKey(to='Role', verbose_name='用户所拥有的角色', blank=True, on_delete=models.CASCADE)

    # 每次创建时，自动将密码设置为密文
    # def save(self, *args, **kwargs):
    #     self.password = hashlib.md5(self.password.encode()).hexdigest()
    #     super(User, self).save(*args, **kwargs)


    class Meta:
        verbose_name = '后台管理员表'
        db_table = verbose_name
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=32, verbose_name='权限')

    # 在admin中改表名
    class Meta:
        verbose_name_plural = '权限表'
        verbose_name = '权限表'
        db_table = verbose_name

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32, unique=True, verbose_name='角色名称')
    permissions = models.ManyToManyField(to='Permission', verbose_name='角色所拥有的权限', blank=True)

    class Meta:
        verbose_name_plural = '角色表'
        verbose_name = '角色表'
        db_table = verbose_name

    def __str__(self):
        return self.name