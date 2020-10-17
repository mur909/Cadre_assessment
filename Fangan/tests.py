import os
from houtai.settings import DATABASES
import pymysql
import itertools


def test():
    obj = Ceping.objects.values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
    for each_obj in obj:
        print('=================================================')
        print('测评人', each_obj['IDcard'])
        print('干部', each_obj['ganBu_unfinished'])
        print('班子', each_obj['banZi_unfinished'])
        gb_code = each_obj['ganBu_unfinished']
        bz_code = each_obj['banZi_unfinished']
        gb_codelst = []
        bz_codelst = []
        # 切片
        for gb in range(0, len(gb_code), 3):
            gb_codelst.append(gb_code[gb:gb + 3])
        print('干部切片', gb_codelst)
        for bz in range(0, len(bz_code), 3):
            bz_codelst.append(bz_code[bz:bz + 3])
        print('班子切片', bz_codelst)
        # 判断是否三个一组
        for each_gb in gb_codelst:
            if len(each_gb) != 3:
                print('干部数据不正常')
                return
        for each_bz in bz_codelst:
            if len(each_bz) != 3:
                print('班子数据不正常！ 数据：{}，长度：{}'.format(each_bz, len(each_bz)))
                return
        # 去重复
        gb_codelst = list(set(gb_codelst))
        bz_codelst = list(set(bz_codelst))
        # 调整顺序
        quickSort(gb_codelst, 0, len(gb_codelst)-1)
        quickSort(bz_codelst, 0, len(bz_codelst) - 1)
        # 转换为字符串
        gb_code = ''
        bz_code = ''
        for each in gb_codelst:
            gb_code = gb_code + each
        for each in bz_codelst:
            bz_code = bz_code + each
        if gb_code != each_obj['ganBu_unfinished']:
            print('干部不正常')
            print('gb_code ===>', gb_code)
            print("each_obj['ganBu_unfinished'] ===>", each_obj['ganBu_unfinished'])
            Ceping.objects.filter(IDcard=each_obj['IDcard']).update(ganBu_unfinished=gb_code)
            return
        if bz_code != each_obj['banZi_unfinished']:
            print('班子不正常')
            Ceping.objects.filter(IDcard=each_obj['IDcard']).update(banZi_unfinished=bz_code)
            return


def test1():
    obj = [{'ganBu_unfinished': '1114222333444555'}, {'ganBu_unfinished': '111222333666444555'}]
    for each_obj in obj:
        gb_code = each_obj['ganBu_unfinished']
        gb_codelst = []
        # 切片
        for gb in range(0, len(gb_code), 3):
            gb_codelst.append(gb_code[gb:gb + 3])
        print('干部切片', gb_codelst)
        # 判断是否三个一组
        for each_gb in gb_codelst:
            if len(each_gb) != 3:
                print('干部数据不正常')
                continue
        # 去重复
        gb_codelst = list(set(gb_codelst))
        # 调整顺序
        quickSort(gb_codelst, 0, len(gb_codelst)-1)
        # 转换为字符串
        gb_code = ''
        for each in gb_codelst:
            gb_code = gb_code + each
        if gb_code != each_obj['ganBu_unfinished']:
            print('干部不正常')
            print('gb_code ===>', gb_code)
            print("each_obj['ganBu_unfinished'] ===>", each_obj['ganBu_unfinished'])
            continue


def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def ganBu_unifinished():
    conn = pymysql.connect(host=DATABASES['default']['HOST'], user=DATABASES['default']['USER'],
                           password=DATABASES['default']['PASSWORD'], database=DATABASES['default']['NAME'],
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select label from 测评人员信息表")
    label = []
    while True:
        row = cursor.fetchone()
        if not row:
            break
        if row == None:
            continue
        # 取出每个人的label字段
        lbl = row[-1]
        if lbl == None:
            continue
        label.append(lbl)
    # print(label)

    # 一个人可能对应多个label的情况
    for i in label:
        n = 0
        m = 0
        if len(i) == 4:
            sql = 'select * from 参评身份 where code = "%s"' % i
            cursor.execute(sql)
            canpingshenfen = cursor.fetchone()
            if not canpingshenfen:
                continue
            # print(canpingshenfen[-2])

            # 根据参评身份去考核关系对应表中获取当前测评身份对应的被测评干部,canpingshenfen[-2]==i
            sql = 'select ganbu_code from 考核关系对应表 where ceping_code = "%s"' % i
            cursor.execute(sql)
            ganbu_code = cursor.fetchone()
            if not ganbu_code:
                continue
            # print(ganbu_code[-2])

            if len(ganbu_code[-1]) == 4:
                post_id = []  # 将post_id以列表形式存储
                post_id1 = []
                sql = "SELECT post_id FROM 被测评人员信息表 WHERE label LIKE '%%{}%%'".format(ganbu_code[-1][m:m + 4])
                cursor.execute(sql)
                beiceping = cursor.fetchall()
                m += 4
                if not beiceping:
                    continue
                for result in beiceping:
                    post_id1.append(result[-1])
                for id in post_id1:
                    if not id in post_id:
                        post_id.append(id)

            else:
                post_id = []  # 将post_id以列表形式存储
                post_id1 = []
                # 对每一个被考核干部代码进行操作
                for num in range(int(len(ganbu_code[-1]) / 4)):
                    # 根据每一个被考核干部代码到被测评人员信息表中找到label符合条件的被测评人
                    sql = "SELECT post_id FROM 被测评人员信息表 WHERE label LIKE '%%{}%%'".format(ganbu_code[-1][m:m + 4])
                    cursor.execute(sql)
                    beiceping = cursor.fetchall()
                    m += 4
                    if not beiceping:
                        continue
                    for result in beiceping:
                        post_id1.append(result[-1])
                    for id in post_id1:
                        if not id in post_id:
                            post_id.append(id)
            # print(post_id)

            # 将post_id合并成一个字符串
            post_ids = "".join(itertools.chain(*post_id))
            # print(post_ids)
            # 将岗位代码添加到测评人员信息表的ganBu_unfinished。
            sql = 'update 测评人员信息表 set ganBu_unfinished="%s" where label = "%s"' % (post_ids, i)
            cursor.execute(sql)
            # 提交数据库执行
            conn.commit()

        # 当一个测评人员有两个身份时
        else:
            print(i)
            post_id1 = []  # 将重复的post_id以列表形式存储
            post_id = []  # post_id去除重复被考核干部代码
            for num in range(int(len(i) / 4)):
                sql = 'select * from 参评身份 where code = "%s"' % i[n:n + 4]
                cursor.execute(sql)
                canpingshenfen = cursor.fetchone()
                print(canpingshenfen)
                if not canpingshenfen:
                    continue
                n += 4

                # 根据参评身份去考核关系对应表中获取当前测评身份对应的被测评干部
                sql = 'select ganbu_code from 考核关系对应表 where ceping_code = "%s"' % i[n:n + 4]
                cursor.execute(sql)
                ganbu_code = cursor.fetchone()
                print(ganbu_code)
                if not ganbu_code:
                    continue
                # print(ganbu_code[-2])

                # 对每一个被考核干部代码进行操作
                m = 0
                for num in range(int(len(ganbu_code[-1]) / 4)):
                    # 根据每一个被考核干部代码到被测评人员信息表中找到label符合条件的被测评人
                    sql = "SELECT post_id FROM 被测评人员信息表 WHERE label LIKE '%%{}%%'".format(ganbu_code[-1][m:m + 4])
                    cursor.execute(sql)
                    beiceping = cursor.fetchall()
                    m += 4
                    if not beiceping:
                        continue
                    for result in beiceping:
                        post_id1.append(result[-1])
                    for id in post_id1:
                        if not id in post_id:
                            post_id.append(id)
            # 将post_id合并成一个字符串
            post_ids = "".join(itertools.chain(*post_id))
            # print(post_ids)
            # 将岗位代码添加到测评人员信息表的ganBu_unfinished。
            sql = 'update 测评人员信息表 set ganBu_unfinished="%s" where label = "%s"' % (post_ids, i)
            cursor.execute(sql)
            # 提交数据库执行
            conn.commit()


def auto():
    id_lst = []
    info = Ceping.objects.filter(zhiwu='科级').values('IDcard', 'department__number', 'label')
    print(info)
    for i in info:
        if int(i['department__number'][0]) == (1 or 2):
            if str(i['label']) == 'None':
                Ceping.objects.filter(IDcard=i['IDcard']).update(label='J004')
            else:
                label = str(i['label']) + 'J004'
                Ceping.objects.filter(IDcard=i['IDcard']).update(label=label)
    print(id_lst)


def a():
    # 51
    ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
        values('department_num_id', 'post_id')
    # 找到所有班子的测评代码
    banzi_obj = BzTjInfo.objects.values('number')
    # 47
    ceping_obj = Ceping.objects. \
        filter(Q(identity='2', zhiwu='教师') | Q(identity='3', zhiwu='教师')). \
        values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
    for each in ceping_obj:
        ganbu_code = each['ganBu_unfinished']
        banzi_code = each['banZi_unfinished']
        for gb in ganbu_obj:
            if each['department__number'] == gb['department_num_id']:
                ganbu_code = ganbu_code + gb['post_id']
        for bz in banzi_obj:
            if each['department__number'] == bz['number'] or \
                    bz['number'] in ('202', '203', '210', '108', '206', '212', '410', '405', '404'):
                banzi_code = banzi_code + bz['number']
        Ceping.objects.filter(IDcard=each['IDcard']). \
            update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Fangan.models import jggbTongji, BzTjInfo, EvaluationItem, xybzIndexWeight
    from Renyuan.models import Ceping, Beiceping
    from django.db.models import Q
    from utils.distribute import update_code

    # ganBu_unifinished()
    # auto()
    # update_code(zhiwu='科级', num=[1, 2], code='J005')
    test1()
