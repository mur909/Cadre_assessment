from django.test import TestCase
import os
import winreg


def get_desktop_path():
    cp_dep = Ceping.objects.values('department').distinct()
    print(cp_dep)
    dep = Department.objects.values('department')
    for i in range(0, len(cp_dep)):
        flag = 0
        for j in range(0, len(dep)):
            if cp_dep[i]['department'] == dep[j]['department']:
                flag = 1
                print(1)
                break
        if flag == 0:
            print(cp_dep[i]['department'])


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Renyuan.models import Ceping, Beiceping
    from Bumen.models import Department

    get_desktop_path()
