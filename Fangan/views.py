from django.db import transaction
from rest_framework.views import APIView
from Renyuan.models import Ceping, Beiceping
from Fangan.models import BzTjInfo, EvaluationItem, xybzIndexWeight, jggbIndexWeight, xygbIndexWeight, zsdwgbIndexWeight, zsdwbzIndexWeight
from django.db.models import Q
from utils.base_response import BaseResponse
from django.http import JsonResponse
import json
from utils.quick_sort import quickSort
from utils.distribute import update_code


class AutoGenerate(APIView):
    def get(self, request):
        """
        考核关系分配
        以下代码为序号为1的考核分配示例，仅供参考
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                Ceping.objects.update(ganBu_finished='', ganBu_unfinished='', banZi_finished='', banZi_unfinished='')
                # 1
                ganbu_code = ''
                banzi_code = ''
                # 全体中层干部
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                # 全部班子
                banzi_obj = BzTjInfo.objects.values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                # 测评人
                ceping_obj = Ceping.objects.filter(
                    Q(zhiwu='校领导') |
                    Q(department__number='103', zhiwu='党群正处') |
                    Q(department__number='102', zhiwu='党群正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                # 遍历每一个测评者
                for each in ceping_obj:
                    # 获取已有的考核代码
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=gb_code,
                                                                        banZi_unfinished=bz_code)

                # 2 and 3
                # 全体中层干部
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                # 所有班子
                banzi_obj = BzTjInfo.objects.values('number')
                # 职务为科长的测评者
                # 如果需要处理本单位，就需要多查询一个department__number
                ceping_obj = Ceping.objects.filter(identity=1, zhiwu='教师'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                # 遍历每一个测评者
                for each in ceping_obj:
                    # 已有的考核代码
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    # 被考核干部
                    for gb in ganbu_obj:
                        # 本单位中层干部
                        if each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    # 被考核班子
                    for bz in banzi_obj:
                        # 判断是否为本单位班子
                        if each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

                # 教师修改（王赟）
                ganbu_code=''
                ganbu_obj= Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_code=''
                ceping_obj = Ceping.objects.filter(Q(zhiwu='教师'))



                # 王赟
                # 序号4（党办主任和宣传部部长）
                ganbu_code = ''
                # 机关全体中层干部
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                # 学院党群正处、党群副处、行政正处
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3']:
                        ganbu_code = ganbu_code + each['post_id']
                # 直属单位党群正处、党群副处、行政正处、行政副处
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['4']:
                        ganbu_code = ganbu_code + each['post_id']
                # 找到被考核班子
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                # 找到所有符合身份的测评人，得到其一卡通号
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='104', zhiwu='党群正处') |
                    Q(department__number='101', zhiwu="党群正处")
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                # 4、对于得到的每一个符合条件的测评人，将上面得到的干部未测评代码和班子未测评代码添加到对应字段
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号5（党办副职、纪委副职、组织部副职、宣传部副职、统战部副职、校友办副职）
                ganbu_code = ''
                # 机关全体中层干部
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                # 学院书记、副书记
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3']:
                        ganbu_code = ganbu_code + each['post_id']
                # 直属单位党群正处、党群副处
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='101', zhiwu='党群副处') |
                    Q(department__number='102', zhiwu="党群副处") |
                    Q(department__number='103', zhiwu='党群副处') |
                    Q(department__number='104', zhiwu='党群副处') |
                    Q(department__number='105', zhiwu='党群副处') |
                    Q(department__number='209', zhiwu='行政副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished', 'department__number')
                for one in ceping_obj:
                    gb_code = ganbu_code + one['ganBu_unfinished']
                    for each in banzi_obj:
                        if one['department__number'] == each['number']:
                            banzi_code = one['banZi_unfinished'] + each['number']
                    Ceping.objects.filter(IDcard=one['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=banzi_code)

                # 序号6
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    # 机关党委书记
                    Q(department__number='103', zhiwu='机关党委书记') |
                    # 分管干部工作的组织部副部长
                    Q(department__number='103', zhiwu='组织部副部长（分管干部工作）')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号7
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                # 1.3、对每一个对象，判断其单位代码是否是1，2，3，4开头，若是就将其岗位代码添加到ganbu_code上
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='105', zhiwu='党群正处') |
                    Q(department__number='209', zhiwu='行政正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号8
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='106', zhiwu='党群正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号9
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='106', zhiwu='党群副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号10
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'] in ['405', '408', '410']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='107', zhiwu='党群正处') |
                    Q(department__number='206', zhiwu='党群正处') |
                    Q(department__number='110', zhiwu='党群正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号11
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'] in ['404']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='108', zhiwu='党群正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号12
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='107', zhiwu='党群副处') |
                    Q(department__number='108', zhiwu='党群副处') |
                    Q(department__number='110', zhiwu='党群副处') |
                    Q(department__number='206', zhiwu='党群副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号13
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'] in ['404', '405', '406', '407', '408', '409', '410']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='109', zhiwu='党群正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号14
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='109', zhiwu='党群副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号15
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='201', zhiwu='行政正处') |
                    Q(department__number='202', zhiwu='行政正处') |
                    Q(department__number='203', zhiwu='行政正处') |
                    Q(department__number='204', zhiwu='行政正处') |
                    Q(department__number='205', zhiwu='行政正处') |
                    Q(department__number='206', zhiwu='行政正处') |
                    Q(department__number='207', zhiwu='行政正处') |
                    Q(department__number='213', zhiwu='行政正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号16
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='201', zhiwu='行政副处') |
                    Q(department__number='202', zhiwu='行政副处') |
                    Q(department__number='203', zhiwu='行政副处') |
                    Q(department__number='204', zhiwu='行政副处') |
                    Q(department__number='205', zhiwu='行政副处') |
                    Q(department__number='206', zhiwu='行政副处') |
                    Q(department__number='207', zhiwu='行政副处') |
                    Q(department__number='213', zhiwu='行政副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号17,原来的18
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2', '4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='210', zhiwu='行政正处') |
                    Q(department__number='211', zhiwu='行政正处') |
                    Q(department__number='214', zhiwu='行政正处') |
                    Q(department__number='215', zhiwu='行政正处') |
                    Q(department__number='216', zhiwu='行政正处') |
                    Q(department__number='208', zhiwu='行政正处') |
                    Q(department__number='212', zhiwu='行政正处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号18，原来的19
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['1', '2']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj:
                    if each['department_num_id'][0] in ['3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['1', '2']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(
                    Q(department__number='210', zhiwu='行政副处') |
                    Q(department__number='211', zhiwu='行政副处') |
                    Q(department__number='214', zhiwu='行政副处') |
                    Q(department__number='215', zhiwu='行政副处') |
                    Q(department__number='216', zhiwu='行政副处') |
                    Q(department__number='208', zhiwu='行政副处') |
                    Q(department__number='212', zhiwu='行政副处')
                ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    Ceping.objects.filter(IDcard=each['IDcard']). \
                        update(ganBu_unfinished=gb_code, banZi_unfinished=bz_code)

                # 序号19，原来的20
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                ganbu_obj1 = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj1:
                    if each['department_num_id'][0] in ['1', '2', '3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj2 = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj2:
                    if each['department_num_id'] in ['101', '102', '103', '104', '105', '106', '109', '209', '404',
                                                     '410', '409']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(identity=2, zhiwu='党群正处'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if each['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 找到设备处的班子和本单位的班子
                    for bz in banzi_obj:
                        if each['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    # 添加代码到每一个测评人
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=gb_code,
                                                                        banZi_unfinished=bz_code)

                # 序号20，原来的22
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                ganbu_obj1 = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj1:
                    if each['department_num_id'][0] in ['1', '2', '3', '4']:
                        ganbu_code = ganbu_code + each['post_id']
                ganbu_obj2 = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for each in ganbu_obj2:
                    if each['department_num_id'] in ['101', '102', '103', '104', '105', '106', '109', '209', '404',
                                                     '410', '409']:
                        ganbu_code = ganbu_code + each['post_id']
                banzi_obj = BzTjInfo.objects.values('number')
                for each in banzi_obj:
                    if each['number'][0] in ['4']:
                        banzi_code = banzi_code + each['number']
                ceping_obj = Ceping.objects.filter(identity=3, zhiwu='党群正处').exclude(department__number='410'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    gb_code = ganbu_code + each['ganBu_unfinished']
                    bz_code = banzi_code + each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if each['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 添加代码到每一个测评人
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=gb_code,
                                                                        banZi_unfinished=bz_code)

                # 9.14
                # 21 and 26
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(department_num_id__in=['322', '323', '324', '401'],
                                                     beiKaoHe__in=['党群副处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ceping_obj = Ceping.objects.filter(department__number='404', zhiwu__in=['党群正处', '行政正处']). \
                    values('IDcard', 'ganBu_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code)

                # 22
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(department_type='机关', beiKaoHe__in=['党群正处', '行政正处']).values(
                    'post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['101', '102', '103', '104', '105', '106', '109', '209'],
                    beiKaoHe__in=['党群副处', '行政副处']
                ).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(department_type='学院', beiKaoHe__in=['党群正处', '行政正处', '行政副处']). \
                    values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_type='直属单位', beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                banzi_obj = BzTjInfo.objects.filter(type='直属单位').values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                ceping_obj = Ceping.objects.filter(department__number='410', zhiwu='党群正处'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 23
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']).values('department_num_id',
                                                                                           'post_id')
                for gb in ganbu_obj:
                    if gb['department_num_id'][0] == '2':
                        if gb['department_num_id'] == '209':
                            continue
                        ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['109', '405', '408', '406', '407'],
                    beiKaoHe__in=['党群副处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                # 直属单位班子
                banzi_obj = BzTjInfo.objects.filter(type='直属单位').values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(identity=2, zhiwu='行政正处'). \
                    values('IDcard', 'department__number', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 24
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id='404', beiKaoHe__in=['党群副处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ceping_obj = Ceping.objects.filter(department__number__in=['322', '323', '324', '401'], zhiwu='行政正处'). \
                    values('IDcard', 'ganBu_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code)

                # 25
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']).values('department_num_id',
                                                                                           'post_id')
                for gb in ganbu_obj:
                    if gb['department_num_id'][0] == '2':
                        if gb['department_num_id'] == '209':
                            continue
                        ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['109', '405', '408', '406', '407'],
                    beiKaoHe__in=['党群副处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                # 直属单位班子
                banzi_obj = BzTjInfo.objects.filter(type='直属单位').values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                # 不含后勤处
                ceping_obj = Ceping.objects.filter(identity=3, zhiwu='行政正处').exclude(department__number='410'). \
                    values('IDcard', 'department__number', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 27
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群副处', '行政副处']).values('department_num_id',
                                                                                           'post_id')
                for gb in ganbu_obj:
                    if gb['department_num_id'][0] == '2':
                        if gb['department_num_id'] == '209':
                            continue
                        ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(department_num_id='109', beiKaoHe__in=['党群副处', '行政副处']).values(
                    'post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                # 直属单位班子
                banzi_obj = BzTjInfo.objects.filter(type='直属单位').values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                ceping_obj = Ceping.objects.filter(department__number='410', zhiwu='行政正处'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 28
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['101', '102', '103', '104', '105', '107', '108', '110', '209'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.filter(
                    number__in=['101', '102', '103', '104', '105', '107', '108', '110', '209']). \
                    values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(identity__in=[2, 3], zhiwu='党群副处'). \
                    values('IDcard', 'department__number', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 29
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(department_num_id='102', beiKaoHe='党群正处').values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(post__contains='组织部部长').values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['201', '202', '203', '206', '204', '205', '213', '410'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.filter(
                    number__in=['201', '202', '203', '206', '204', '205', '213', '410']). \
                    values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                # 不包含后勤处
                ceping_obj = Ceping.objects.filter(identity__in=[2, 3], zhiwu='行政副处').exclude(department__number='410'). \
                    values('IDcard', 'department__number', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 30
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(department_num_id='102', beiKaoHe='党群正处').values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(post__contains='组织部部长').values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['201', '202', '203', '206', '204', '205', '213'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(department_type__in=['学院', '直属单位'], beiKaoHe__in=['行政正处', '行政副处']). \
                    values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                banzi_obj = BzTjInfo.objects.filter(number__in=['201', '202', '203', '206', '204', '205', '213']). \
                    values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                # 不包含后勤处
                ceping_obj = Ceping.objects.filter(department__number='410', zhiwu='行政副处'). \
                    values('IDcard', 'department__number', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 31 互评
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['404', '401', '322', '323', '324'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('IDcard', 'post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                for gb in ganbu_obj:
                    gb_code = ganbu_code
                    ceping_obj = Ceping.objects.filter(IDcard=gb['IDcard']).values('IDcard', 'ganBu_unfinished')
                    if ceping_obj:
                        gb_code = gb_code.replace(gb['post_id'], '')
                        gb_code = gb_code + ceping_obj[0]['ganBu_unfinished']
                        Ceping.objects.filter(IDcard=ceping_obj[0]['IDcard']).update(ganBu_unfinished=gb_code)

                # 32 互评
                ganbu_code = ''
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['406', '407'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('IDcard', 'post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                for gb in ganbu_obj:
                    gb_code = ganbu_code
                    ceping_obj = Ceping.objects.filter(IDcard=gb['IDcard']).values('IDcard', 'ganBu_unfinished')
                    if ceping_obj:
                        gb_code = gb_code.replace(gb['post_id'], '')
                        gb_code = gb_code + ceping_obj[0]['ganBu_unfinished']
                        Ceping.objects.filter(IDcard=ceping_obj[0]['IDcard']).update(ganBu_unfinished=gb_code)

                # 33
                ganbu_code = ''
                banzi_code = ''
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['101', '106', '208', '212', '404', '405', '409', '410'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                for gb in ganbu_obj:
                    if gb['department_num_id'][0] == '2':
                        ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.filter(number__in=['208', '212', '404', '405', '409', '410']). \
                    values('number')
                for bz in banzi_obj:
                    banzi_code = banzi_code + bz['number']
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='T'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 34
                ganbu_code = ''
                banzi_code = '103'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id='103', beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='A'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 35
                ganbu_code = ''
                banzi_code = '107108110'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['107', '110', '108'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id='206', beiKaoHe__in=['党群正处', '党群副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='B'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 36
                ganbu_code = ''
                banzi_code = '109'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id='109', beiKaoHe__in=['党群正处', '党群副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='C'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 37
                ganbu_code = ''
                banzi_code = '207210211214216410'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['207', '210', '211', '214', '216', '410'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='D'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 38
                ganbu_code = ''
                banzi_code = '203208408'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['203', '208', '408'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='E'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 39
                ganbu_code = ''
                banzi_code = '204205325'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['204', '205', '325'],
                    beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']).values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='F'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 40
                ganbu_code = ''
                banzi_code = '206'
                ganbu_obj = Beiceping.objects.filter(
                    department_num_id__in=['206'],
                    beiKaoHe__in=['行政正处', '行政副处']).values('post', 'post_id')
                for gb in ganbu_obj:
                    if '党委研究生工作部部长' in gb['post']:
                        continue
                    ganbu_code = ganbu_code + gb['post_id']
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('department_num_id', 'post_id')
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(special_identity__contains='G'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    for gb in ganbu_obj:
                        if cp['department__number'] == gb['department_num_id']:
                            gb_code = gb_code + gb['post_id']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 41
                # 首先找到全体中层干部的单位代码和岗位代码
                ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
                    values('department_num_id', 'post_id')
                # 找到所有班子的测评代码
                banzi_obj = BzTjInfo.objects.values('number')
                # 找到特殊人员代码中包含H也就是设备管理员的测评人的单位代码和一卡通
                ceping_obj = Ceping.objects.filter(special_identity__contains='H'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                # 对每一个测评人遍历
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    # 找到设备处的中层干部和本单位的中层干部
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '213' or each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    # 找到设备处的班子和本单位的班子
                    for bz in banzi_obj:
                        if bz['number'] == '213' or each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    # 添加代码到每一个测评人
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 42
                ceping_obj = Ceping.objects.filter(special_identity__contains='I'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    # 找到设备处的中层干部和本单位的中层干部
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '102' or each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    # 找到设备处的班子和本单位的班子
                    for bz in banzi_obj:
                        if bz['number'] == '102' or each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    # 添加代码到每一个测评人
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 43
                ceping_obj = Ceping.objects.filter(special_identity__contains='J'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '202' or each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == '202' or each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 44
                ceping_obj = Ceping.objects.filter(special_identity__contains='K'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '104' or each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == '104' or each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 45
                ceping_obj = Ceping.objects. \
                    filter(identity__in=[2, 3], zhiwu='教师'). \
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

                # 46
                ceping_obj = Ceping.objects.filter(special_identity__contains='L'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if each['department__number'] == bz['number'] or \
                                bz['number'] in ('107', '108', '110', '203', '212', '210', '404', '410'):
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 47
                ceping_obj = Ceping.objects.filter(special_identity__contains='M'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if each['department__number'] == bz['number'] or \
                                bz['number'] in ('107', '108', '110', '203', '206', '212', '210', '404', '410'):
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 48
                ceping_obj = Ceping.objects.filter(special_identity__contains='N'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == ('406' or '408'):
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == ('406' or '408'):
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 49 and 50
                ceping_obj = Ceping.objects.filter(
                    Q(special_identity__contains='O') | Q(special_identity__contains='P')). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '214':
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == '214':
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 51
                ceping_obj = Ceping.objects.filter(special_identity__contains='Q'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == '105':
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == '105':
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 52
                ceping_obj = Ceping.objects.filter(special_identity__contains='R'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if gb['department_num_id'] == ('406' or '407'):
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if bz['number'] == ('406' or '407'):
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 53
                ceping_obj = Ceping.objects.filter(special_identity__contains='S'). \
                    values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for each in ceping_obj:
                    ganbu_code = each['ganBu_unfinished']
                    banzi_code = each['banZi_unfinished']
                    for gb in ganbu_obj:
                        if each['department__number'] == gb['department_num_id']:
                            ganbu_code = ganbu_code + gb['post_id']
                    for bz in banzi_obj:
                        if each['department__number'] == bz['number']:
                            banzi_code = banzi_code + bz['number']
                    Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                        banZi_unfinished=banzi_code)

                # 54.1 财务处派驻人员
                ganbu_code = ''
                banzi_code = '403'
                ganbu_obj = Beiceping.objects.filter(department_num_id='403',
                                                     beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ceping_obj = Ceping.objects.filter(special_identity__contains='U'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 54.2 财务处派驻人员
                ganbu_code = ''
                banzi_code = '410'
                ganbu_obj = Beiceping.objects.filter(department_num_id='410',
                                                     beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ceping_obj = Ceping.objects.filter(special_identity__contains='V'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 54.3 财务处派驻人员
                ganbu_code = ''
                banzi_code = '408'
                ganbu_obj = Beiceping.objects.filter(department_num_id='408',
                                                     beiKaoHe__in=['党群正处', '行政正处', '党群副处', '行政副处']). \
                    values('post_id')
                for gb in ganbu_obj:
                    ganbu_code = ganbu_code + gb['post_id']
                ceping_obj = Ceping.objects.filter(special_identity__contains='W'). \
                    values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
                for cp in ceping_obj:
                    gb_code = ganbu_code + cp['ganBu_unfinished']
                    bz_code = banzi_code + cp['banZi_unfinished']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)

                # 55
                banzi_code = ''
                banzi_obj = BzTjInfo.objects.values('number')
                ceping_obj = Ceping.objects.filter(identity__in=[2, 3]).values('department__number', 'IDcard',
                                                                               'banZi_unfinished')
                for cp in ceping_obj:
                    bz_code = banzi_code + cp['banZi_unfinished']
                    # 本单位的班子
                    for bz in banzi_obj:
                        if cp['department__number'] == bz['number']:
                            bz_code = bz_code + bz['number']
                    Ceping.objects.filter(IDcard=cp['IDcard']).update(ganBu_unfinished=gb_code,
                                                                      banZi_unfinished=bz_code)
        except Exception as e:
            print(e)
            ret.code = 0
            ret.error = '生成失败'
            return JsonResponse(ret.dict)
        ret.code = 1
        ret.data = '生成成功'
        return JsonResponse(ret.dict)


class CheckCode(APIView):
    def get(self, request):
        """
        生成的代码校验
        :return:
        """
        try:
            ret = BaseResponse()
            num = 0
            obj = Ceping.objects.values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
            for each_obj in obj:
                gb_code = each_obj['ganBu_unfinished']
                bz_code = each_obj['banZi_unfinished']
                gb_codelst = []
                bz_codelst = []
                # 切片
                for gb in range(0, len(gb_code), 3):
                    gb_codelst.append(gb_code[gb:gb + 3])
                for bz in range(0, len(bz_code), 3):
                    bz_codelst.append(bz_code[bz:bz + 3])
                # 判断是否三个一组
                for each_gb in gb_codelst:
                    if len(each_gb) != 3:
                        ret.code = 1
                        ret.data = '一卡通号：{}，干部未测评数据不正常，请检查！'.format(each_obj['IDcard'])
                        return JsonResponse(ret.dict)
                for each_bz in bz_codelst:
                    if len(each_bz) != 3:
                        ret.code = 1
                        ret.data = '一卡通号：{}，班子未测评数据不正常，请检查！'.format(each_obj['IDcard'])
                        return JsonResponse(ret.dict)
                # 去重复
                gb_codelst = list(set(gb_codelst))
                bz_codelst = list(set(bz_codelst))
                # 调整顺序
                quickSort(gb_codelst, 0, len(gb_codelst) - 1)
                quickSort(bz_codelst, 0, len(bz_codelst) - 1)
                # 转换为字符串
                gb_code = ''
                bz_code = ''
                for each in gb_codelst:
                    gb_code = gb_code + each
                for each in bz_codelst:
                    bz_code = bz_code + each
                if gb_code != each_obj['ganBu_unfinished']:
                    Ceping.objects.filter(IDcard=each_obj['IDcard']).update(ganBu_unfinished=gb_code)
                    num = num + 1
                if bz_code != each_obj['banZi_unfinished']:
                    Ceping.objects.filter(IDcard=each_obj['IDcard']).update(banZi_unfinished=bz_code)
                    num = num + 1
        except Exception as e:
            ret.code = 0
            ret.error = '代码检查出现异常'
            return JsonResponse(ret.dict)
        ret.code = 1
        ret.data = '代码检查完毕，共纠正【{}】条数据。'.format(num)
        return JsonResponse(ret.dict)


class EvaluateScore(APIView):
    # 获取所有测评项
    def get(self, request):
        try:
            obj_evaluate = EvaluationItem.objects.all().values()
            evaluate = list(obj_evaluate)
            return JsonResponse({'code': 1, 'data': evaluate})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "获取测评项信息出现异常，具体错误：" + str(e)})

    # 修改测评分数
    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            pk = data['id']
            score = data['score']
            try:
                score = int(score)
            except Exception as e:
                return JsonResponse({'code': 0, 'msg': "修改分数应为整数"})
            if 0 <= score <= 100:
                obj_evaluate = EvaluationItem.objects.get(id=pk)
                obj_evaluate.score = score
                obj_evaluate.save()
                evaluate = EvaluationItem.objects.all().values()
                evaluate = list(evaluate)
                return JsonResponse({'code': 1, 'data': evaluate})
            else:
                return JsonResponse({'code': 0, 'msg': "分数应位于0-100之间"})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "获取测评项信息出现异常，具体错误：" + str(e)})


class Weight(APIView):
    def get(self, request, DB):
        try:
            DB = globals()[DB]
            objs = DB.objects.all().values('index', 'weight', 'code')
            objs = list(objs)
            return JsonResponse({'code': 1, 'data': objs})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "获取学院班子指标权重出现异常，具体错误：" + str(e)})

    def post(self, request, DB):
        try:
            DB = globals()[DB]
            data = json.loads(request.body.decode("utf-8"))
            # 判断权重信息是否完整
            for one_data in data:
                if (one_data['index'] and one_data['weight'] == None) or (one_data['index'] == None and one_data['weight']):
                    return JsonResponse({'code': 0, 'msg': "权重信息不完整"})
            # 若权重信息完整，则计算权重和，并判断是否为1
            sum = 0.0
            for one_data in data:
                if one_data['weight']:
                    sum += float(one_data['weight'])
            if 1 > sum > 0.999:
                sum = 1
            if sum != 1:
                return JsonResponse({'code': 0, 'msg': "权重和需为1"})
            # 权重信息符合规范，写入数据库
            if sum == 1:
                for one_data in data:
                    DB.objects.filter(code=one_data['code']).update(index=one_data['index'], weight=one_data['weight'])
            objs = DB.objects.all().values('index', 'weight')
            objs = list(objs)
            return JsonResponse({'code': 1, 'data': objs})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "提交学院班子指标权重出现异常，具体错误：" + str(e)})
