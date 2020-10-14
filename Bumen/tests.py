from django.test import TestCase
import os, random



def a():
    dep_num = Ceping.objects.filter(IDcard='1000004707').values('department__number')  # 测评人单位代码
    print(dep_num)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Renyuan.models import Ceping

    a()
