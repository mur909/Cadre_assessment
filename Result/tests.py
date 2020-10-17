from django.test import TestCase

# Create your tests here.
import os


def test():
    result = xygbResult.objects.values('beiceping_id__name')
    print(result)


def test1():
    category = []
    category_obj = Gbresult.objects.values_list('department').distinct()
    for i in category_obj:
        category.append(i[0])
    for i in category:
        dep_obj = Gbresult.objects.filter(department=i).values('IDcard', 'score').order_by('score').reverse()
        print(dep_obj)
        for j in range(0, len(dep_obj)):
            Gbresult.objects.filter(IDcard=dep_obj[j]['IDcard']).update(rankingOfDep=j + 1)


def test2():
    index_weight = []
    index_obj = xygbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])
    print(index_weight)
    print(len(index_weight))
    index19_weight = GbCpWeight.objects.filter(code='001').values_list('weight', flat=True)[0]  # 学院校领导
    index20_weight = GbCpWeight.objects.filter(code='002').values_list('weight', flat=True)[0]  # 班子成员
    index21_weight = GbCpWeight.objects.filter(code='003').values_list('weight', flat=True)[0]  # 学院师生
    index22_weight = GbCpWeight.objects.filter(code='004').values_list('weight', flat=True)[0]  # 对口机关
    print(index19_weight, index20_weight, index21_weight, index22_weight)
    beiceping_id = xygbTongji.objects.values_list('beiceping_id').distinct()
    print(beiceping_id)


def test3():
    index_weight = []
    index_obj = jggbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])
    print(index_weight)
    print(len(index_weight))
    index19_weight = GbCpWeight.objects.filter(code='005').values_list('weight', flat=True)[0]  # 机关校领导权重
    index20_weight = GbCpWeight.objects.filter(code='006').values_list('weight', flat=True)[0]  # 党政处级权重
    index21_weight = GbCpWeight.objects.filter(code='007').values_list('weight', flat=True)[0]  # 党政科级及职工权重
    index22_weight = GbCpWeight.objects.filter(code='008').values_list('weight', flat=True)[0]  # 学院领导权重
    index23_weight = GbCpWeight.objects.filter(code='009').values_list('weight', flat=True)[0]  # 学院相关权重
    print(index19_weight, index20_weight, index21_weight, index22_weight, index23_weight)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Fangan.models import jggbTongji, xygbIndexWeight, GbCpWeight, xygbTongji, jggbIndexWeight, jggbResult, xygbResult
    from Result.models import Gbresult

    test()
    # test1()
    # test2()
    # test3()