import json
from django.views import View
from rest_framework.views import APIView
from Renyuan.models import Ceping, Beiceping
from Fangan.models import BzTjInfo,EvaluationItem,xybzIndexWeight,zsdwbzIndexWeight,jggbIndexWeight,xygbIndexWeight,zsdwgbIndexWeight
from django.db.models import Q
from utils.base_response import BaseResponse
from django.http import JsonResponse
from django.db.models import Sum
from utils.distribute import update_code
from decimal import Decimal


class AutoGenerate(APIView):
    def get(self, request):
        """
        考核关系分配
        以下代码为序号为1的考核分配示例，仅供参考
        :param request:
        :return:
        """
        # 1
        # 全体中层干部
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        # 全部班子
        banzi_obj = BzTjInfo.objects.values('number')
        # 测评人
        ceping_obj = Ceping.objects.filter(
            Q(zhiwu='校领导') |
            Q(department__number='103', zhiwu='党群正处') |
            Q(department__number='102', zhiwu='党群正处')
        ).values('IDcard', 'ganBu_unfinished', 'banZi_unfinished')
        # 遍历每一个测评者
        for each in ceping_obj:
            # 获取已有的考核代码
            ganbu_code = each['ganBu_unfinished']
            banzi_code = each['banZi_unfinished']
            # 被考核干部代码
            for gb in ganbu_obj:
                if gb['department_num_id'][0] in ['1', '2', '3', '4']:
                    ganbu_code = ganbu_code + gb['post_id']
            # 被考核班子代码
            for bz in banzi_obj:
                if bz['number'][0] in ['1', '2', '3', '4']:
                    banzi_code = banzi_code + bz['number']
            # 添加考核代码到测评人
            Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                banZi_unfinished=banzi_code)

        # 2
        # 全体中层干部
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        # 所有班子
        banzi_obj = BzTjInfo.objects.values('number')
        # 职务为科长的测评者
        # 如果需要处理本单位，就需要多查询一个department__number
        ceping_obj = Ceping.objects.filter(zhiwu='教师'). \
            values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
        # 遍历每一个测评者
        for each in ceping_obj:
            # 1，2开头且职务为科长的测评者
            if each['department__number'][0] in ['1', '2']:
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

        # 3
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        banzi_obj = BzTjInfo.objects.values('number')
        ceping_obj = Ceping.objects.filter(zhiwu='教师'). \
            values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
        for each in ceping_obj:
            if each['department__number'][0] in ['1', '2']:
                ganbu_code = each['ganBu_unfinished']
                banzi_code = each['banZi_unfinished']
                for gb in ganbu_obj:
                    if each['department__number'] == gb['department_num_id']:
                        ganbu_code = ganbu_code + gb['post_id']
                for bz in banzi_obj:
                    if each['department__number'] == bz['number']:
                        banzi_code = banzi_code + bz['number']
                Ceping.objects.filter(IDcard=each['IDcard']). \
                    update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + one['ganBu_unfinished']
            for each in banzi_obj:
                if one['department__number'] == each['number']:
                    banzi_code = one['banZi_unfinished'] + each['number']
            Ceping.objects.filter(IDcard=one['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

        # 序号6
        ganbu_code = ''
        ganbu_obj = Beiceping.objects.filter(beikaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        for each in ganbu_obj:
            if each['department_num_id'][0] in ['1', '2']:
                ganbu_code = ganbu_code + each['post_id']
        ganbu_obj = Beiceping.objects.filter(beikaoHe__in=['党群正处', '党群副处', '行政正处']). \
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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

        # 序号7
        ganbu_code = ''
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        # 1.3、对每一个对象，判断其单位代码是否是1，2，3，4开头，若是就将其岗位代码添加到ganbu_code上
        for each in ganbu_obj:
            if each['department_num_id'][0] in ['1', '2']:
                ganbu_code = ganbu_code + each['post_id']
        ganbu_obj = Beiceping.objects.filter(beikaoHe__in=['党群正处', '党群副处', '行政正处']). \
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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

        # 序号10
        ganbu_code = ''
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')
        for each in ganbu_obj:
            if each['department_num_id'][0] in ['1', '2']:
                ganbu_code = ganbu_code + each['post_id']
        ganbu_obj = Beiceping.objects.filter(beikaoHe__in=['党群正处', '党群副处', '行政正处']). \
            values('department_num_id', 'post_id')
        for each in ganbu_obj:
            if each['department_num_id'][0] in ['3', '4']:
                ganbu_code = ganbu_code + each['post_id']
        ganbu_obj = Beiceping.objects.filter(beikaoHe__in=['行政副处']). \
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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            Ceping.objects.filter(IDcard=each['IDcard']). \
                update(ganBu_unfinished=ganbu_code, banZi_unfinished=banzi_code)

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
            if each['department_num_id'] in ['101', '102', '103', '104', '105', '106', '109', '209', '404', '410', '409']:
                ganbu_code = ganbu_code + each['post_id']
        banzi_obj = BzTjInfo.objects.values('number')
        for each in banzi_obj:
            if each['number'][0] in ['4']:
                banzi_code = banzi_code + each['number']
        ceping_obj = Ceping.objects.filter(identity=2, zhiwu='党群正处'). \
            values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
        for each in ceping_obj:
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            for gb in ganbu_obj:
                if each['department__number'] == gb['department_num_id']:
                    ganbu_code = ganbu_code + gb['post_id']
            # 找到设备处的班子和本单位的班子
            for bz in banzi_obj:
                if each['department__number'] == bz['number']:
                    banzi_code = banzi_code + bz['number']
            # 添加代码到每一个测评人
            Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                banZi_unfinished=banzi_code)

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
            if each['department_num_id'] in ['101', '102', '103', '104', '105', '106', '109', '209', '404', '410', '409']:
                ganbu_code = ganbu_code + each['post_id']
        banzi_obj = BzTjInfo.objects.values('number')
        for each in banzi_obj:
            if each['number'][0] in ['4']:
                banzi_code = banzi_code + each['number']
        ceping_obj = Ceping.objects.filter(identity=3, zhiwu='党群正处'). \
            values('department__number', 'IDcard', 'ganBu_unfinished', 'banZi_unfinished')
        for each in ceping_obj:
            ganbu_code = ganbu_code + each['ganBu_unfinished']
            banzi_code = banzi_code + each['banZi_unfinished']
            for gb in ganbu_obj:
                if each['department__number'] == gb['department_num_id']:
                    ganbu_code = ganbu_code + gb['post_id']
            # 添加代码到每一个测评人
            Ceping.objects.filter(IDcard=each['IDcard']).update(ganBu_unfinished=ganbu_code,
                                                                banZi_unfinished=banzi_code)

        # 21
        ganbu_code = ''
        banzi_code = ''
        ganbu_obj = Beiceping.objects.filter(beiKaoHe__in=['党群正处', '党群副处', '行政正处', '行政副处']). \
            values('department_num_id', 'post_id')


        # 43
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

        # 44
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

        # 45
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

        # 46
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

        # 48
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

        # 49
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

        # 50
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

        # 51+52
        ceping_obj = Ceping.objects.filter(Q(special_identity__contains='O') | Q(special_identity__contains='P')). \
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

        # 53
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

        # 54
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

        # 55
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

        # 56
        ceping_obj = Ceping.objects.filter(special_identity__contains='T'). \
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

# 测评项分数修改
class EvaluateScore(View):
    # 获取所有测评项
    def get(self,request):
        try:
            obj_evaluate=EvaluationItem.objects.all().values()
            evaluate=list(obj_evaluate)
            return JsonResponse({'code': 1, 'data': evaluate})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"获取测评项信息出现异常，具体错误：" + str(e)})
    # 修改测评分数
    def post(self,request):
        try:
            data=json.loads(request.body.decode("utf-8"))
            pk=data['id']
            score=data['score']
            try:
                score=int(score)
            except Exception as e:
                return JsonResponse({'code':0,'msg':"修改分数应为整数" })
            if 0<=score<=100:
                obj_evaluate=EvaluationItem.objects.get(id=pk)
                obj_evaluate.score=score
                obj_evaluate.save()
                evaluate=EvaluationItem.objects.all().values()
                evaluate=list(evaluate)
                return JsonResponse({'code': 1, 'data': evaluate})
            else:
                return JsonResponse({'code':0,'msg':"分数应位于0-100之间"})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"获取测评项信息出现异常，具体错误：" + str(e)})

"""
# 学院班子指标权重表
class Weight(View):
    def get(self,request):
        try:
            objs=xybzIndexWeight.objects.all().values('index','weight','code')
            objs=list(objs)
            return JsonResponse({'code':1,'data':objs})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"获取学院班子指标权重出现异常，具体错误：" + str(e)})

    def post(self,request):
        try:
            data=json.loads(request.body.decode("utf-8"))
            # 判断权重信息是否完整
            for one_data in data:
                if (one_data['index'] and one_data['weight'] == '') or (one_data['index'] == '' and one_data['weight']):
                    return JsonResponse({'code': 0, 'msg': "权重信息不完整" })
            # 若权重信息完整，则计算权重和，并判断是否为1
            sum=0.0
            for one_data in data:
                if one_data['weight']:
                    sum+=float(one_data['weight'])
            if sum>0.999:
                sum=1
            if sum!=1:
                return JsonResponse({'code': 0, 'msg': "权重和需为1"})
            # 权重信息符合规范，写入数据库
            try:
                for one_data in data:
                    obj=xybzIndexWeight.objects.filter(code=one_data['code']).update(index=one_data['index'],weight=one_data['weight'])
                objs=xybzIndexWeight.objects.all().values('index','weight')
                objs=list(objs)
                return JsonResponse({'code':1,'data':objs})
            except Exception as e:
                return JsonResponse({'code': 0, 'msg': "保存学院班子指标权重出现异常，具体错误：" + str(e)})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"提交学院班子指标权重出现异常，具体错误：" + str(e)})
"""

class Weight(View):
    def get(self,request,DB):
        try:
            DB=globals()[DB]
            objs=DB.objects.all().values('index','weight','code')
            objs=list(objs)
            return JsonResponse({'code':1,'data':objs})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"获取学院班子指标权重出现异常，具体错误：" + str(e)})

    def post(self,request,DB):
        try:
            DB=globals()[DB]
            data=json.loads(request.body.decode("utf-8"))
            # 判断权重信息是否完整
            for one_data in data:
                if (one_data['index'] and one_data['weight'] == '') or (one_data['index'] == '' and one_data['weight']):
                    return JsonResponse({'code': 0, 'msg': "权重信息不完整" })
            # 若权重信息完整，则计算权重和，并判断是否为1
            sum=0.0
            for one_data in data:
                if one_data['weight']:
                    sum+=float(one_data['weight'])
            if sum>0.999:
                sum=1
            if sum!=1:
                return JsonResponse({'code': 0, 'msg': "权重和需为1"})
            # 权重信息符合规范，写入数据库
            try:
                for one_data in data:
                    obj=DB.objects.filter(code=one_data['code']).update(index=one_data['index'],weight=one_data['weight'])
                objs=DB.objects.all().values('index','weight')
                objs=list(objs)
                return JsonResponse({'code':1,'data':objs})
            except Exception as e:
                return JsonResponse({'code': 0, 'msg': "保存学院班子指标权重出现异常，具体错误：" + str(e)})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"提交学院班子指标权重出现异常，具体错误：" + str(e)})