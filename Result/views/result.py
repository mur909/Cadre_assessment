from rest_framework.response import Response
from rest_framework.views import APIView
from Fangan.models import xygbResult, jggbResult, zsdwgbResult, xybzResult, zsdwbzResult, BzTjInfo
from Renyuan.models import Beiceping
from Result.models import Gbresult, Bzresult
from utils.base_response import BaseResponse
from utils.calculation import jggbresult, xygbresult, zsdwgbresult, xybzresult, zsdwbzresult
import datetime
from django.db import transaction


class XygbresultView(APIView):
    def post(self, request):
        """
        学院干部结果表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                xygbResult.objects.all().delete()
                xygbresult()
        except Exception as e:
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class JggbresultView(APIView):
    def post(self, request):
        """
        # 机关干部结果表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                jggbResult.objects.all().delete()
                jggbresult()
        except Exception as e:
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class ZsdwgbresultView(APIView):
    def post(self, request):
        """
        直属单位干部结果表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                zsdwgbResult.objects.all().delete()
                zsdwgbresult()
        except Exception as e:
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class XybzresultView(APIView):
    def post(self, request):
        """
        学院班子结果表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                xybzResult.objects.all().delete()
                xybzresult()
        except Exception as e:
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class ZsdwbzresultView(APIView):
    def post(self, request):
        """
        直属单位班子结果表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            with transaction.atomic():
                zsdwbzResult.objects.all().delete()
                zsdwbzresult()
        except Exception as e:
            print(e)
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class Result_all(APIView):
    def get(self, request):
        """计算所有表"""
        ret = BaseResponse()
        try:
            with transaction.atomic():
                jggbResult.objects.all().delete()
                jggbresult()
                xygbResult.objects.all().delete()
                xygbresult()
                zsdwgbResult.objects.all().delete()
                zsdwgbresult()
                xybzResult.objects.all().delete()
                xybzresult()
                zsdwbzResult.objects.all().delete()
                zsdwbzresult()
        except Exception as e:
            print(e)
            ret.code = 204
            ret.error = '数据计算失败'
            return Response(ret.dict)
        ret.code = 203
        ret.data = '数据计算成功'
        return Response(ret.dict)


class Gb_of_all(APIView):
    def get(self, request):
        """
        干部考核汇总表
        将三张干部考核结果表的数据汇总在一起，并计算排名
        """
        ret = BaseResponse()

        try:
            with transaction.atomic():
                year = datetime.datetime.now().year  # 当前年份
                # 计算前，首先删除当前年份的数据
                Gbresult.objects.filter(year=year).all().delete()

                xy_obj = xygbResult.objects.filter(level='全体').values()  # 学院干部结果表
                jg_obj = jggbResult.objects.filter(level='全体').values()  # 机关干部结果表
                zsdw_obj = zsdwgbResult.objects.filter(level='全体').values()  # 直属单位干部结果表

                # 处理机关干部结果表
                for i in range(0, len(jg_obj)):
                    each_obj = Beiceping.objects.filter(IDcard=jg_obj[i]['beiceping_id']).\
                        values('name', 'department_id', 'beiKaoHe')  # 姓名, 单位名
                    # 将机关干部结果表的内容添加到干部结果汇总表中
                    Gbresult.objects.create(
                        name=each_obj[0]['name'],
                        IDcard=jg_obj[i]['beiceping_id'],
                        department=each_obj[0]['department_id'],
                        category='机关',
                        beiKaoHe=each_obj[0]['beiKaoHe'],
                        year=year,
                        index1=jg_obj[i]['index1'],
                        index2=jg_obj[i]['index2'],
                        index3=jg_obj[i]['index3'],
                        index4=jg_obj[i]['index4'],
                        index5=jg_obj[i]['index5'],
                        index6=jg_obj[i]['index6'],
                        index7=jg_obj[i]['index7'],
                        index8=jg_obj[i]['index8'],
                        index9=jg_obj[i]['index9'],
                        index10=jg_obj[i]['index10'],
                        index11=jg_obj[i]['index11'],
                        index12=jg_obj[i]['index12'],
                        index13=jg_obj[i]['index13'],
                        index14=jg_obj[i]['index14'],
                        index15=jg_obj[i]['index15'],
                        index16=jg_obj[i]['index16'],
                        index17=jg_obj[i]['index17'],
                        index18=jg_obj[i]['index18'],
                        index19=jg_obj[i]['index19'],
                        index20=jg_obj[i]['index20'],
                        index21=jg_obj[i]['index21'],
                        index22=jg_obj[i]['index22'],
                        index23=jg_obj[i]['index23'],
                        Excellent=0,
                        score=jg_obj[i]['score']
                    )
                # 处理学院干部结果表
                for i in range(0, len(xy_obj)):
                    each_obj = Beiceping.objects.filter(IDcard=xy_obj[i]['beiceping_id']).\
                        values('name', 'department_id', 'beiKaoHe')  # 姓名, 单位名
                    # 将学院干部结果表的内容添加到干部结果汇总表中
                    Gbresult.objects.create(
                        name=each_obj[0]['name'],
                        IDcard=xy_obj[i]['beiceping_id'],
                        department=each_obj[0]['department_id'],
                        category='学院',
                        beiKaoHe=each_obj[0]['beiKaoHe'],
                        year=year,
                        index1=xy_obj[i]['index1'],
                        index2=xy_obj[i]['index2'],
                        index3=xy_obj[i]['index3'],
                        index4=xy_obj[i]['index4'],
                        index5=xy_obj[i]['index5'],
                        index6=xy_obj[i]['index6'],
                        index7=xy_obj[i]['index7'],
                        index8=xy_obj[i]['index8'],
                        index9=xy_obj[i]['index9'],
                        index10=xy_obj[i]['index10'],
                        index11=xy_obj[i]['index11'],
                        index12=xy_obj[i]['index12'],
                        index13=xy_obj[i]['index13'],
                        index14=xy_obj[i]['index14'],
                        index15=xy_obj[i]['index15'],
                        index16=xy_obj[i]['index16'],
                        index17=xy_obj[i]['index17'],
                        index18=xy_obj[i]['index18'],
                        index19=xy_obj[i]['index19'],
                        index20=xy_obj[i]['index20'],
                        index21=xy_obj[i]['index21'],
                        index22=xy_obj[i]['index22'],
                        Excellent=0,
                        score=xy_obj[i]['score']
                    )
                # 处理直属单位干部结果表
                for i in range(0, len(zsdw_obj)):
                    each_obj = Beiceping.objects.filter(IDcard=zsdw_obj[i]['beiceping_id']).\
                        values('name', 'department_id', 'beiKaoHe')  # 姓名, 单位名
                    # 将直属单位干部结果表内容添加到干部结果汇总表中
                    Gbresult.objects.create(
                        name=each_obj[0]['name'],
                        IDcard=zsdw_obj[i]['beiceping_id'],
                        department=each_obj[0]['department_id'],
                        category='直属单位',
                        beiKaoHe=each_obj[0]['beiKaoHe'],
                        year=year,
                        index1=zsdw_obj[i]['index1'],
                        index2=zsdw_obj[i]['index2'],
                        index3=zsdw_obj[i]['index3'],
                        index4=zsdw_obj[i]['index4'],
                        index5=zsdw_obj[i]['index5'],
                        index6=zsdw_obj[i]['index6'],
                        index7=zsdw_obj[i]['index7'],
                        index8=zsdw_obj[i]['index8'],
                        index9=zsdw_obj[i]['index9'],
                        index10=zsdw_obj[i]['index10'],
                        index11=zsdw_obj[i]['index11'],
                        index12=zsdw_obj[i]['index12'],
                        index13=zsdw_obj[i]['index13'],
                        index14=zsdw_obj[i]['index14'],
                        index15=zsdw_obj[i]['index15'],
                        index16=zsdw_obj[i]['index16'],
                        index17=zsdw_obj[i]['index17'],
                        index18=zsdw_obj[i]['index18'],
                        index19=zsdw_obj[i]['index19'],
                        index20=zsdw_obj[i]['index20'],
                        index21=zsdw_obj[i]['index21'],
                        index22=zsdw_obj[i]['index22'],
                        index23=zsdw_obj[i]['index23'],
                        Excellent=0,
                        score=zsdw_obj[i]['score']
                    )

                # 综合排名
                gb_obj = Gbresult.objects.values('IDcard', 'score').order_by('score').reverse()
                for i in range(0, len(gb_obj)):
                    Gbresult.objects.filter(IDcard=gb_obj[i]['IDcard']).update(rankingOfAll=i+1)

                # 学院排名
                xy_obj = Gbresult.objects.filter(category='学院').values('IDcard', 'score').order_by('score').reverse()
                for i in range(0, len(xy_obj)):
                    Gbresult.objects.filter(IDcard=xy_obj[i]['IDcard']).update(rankingofCategory=i+1)
                # 机关排名
                jg_obj = Gbresult.objects.filter(category='机关').values('IDcard', 'score').order_by('score').reverse()
                for i in range(0, len(jg_obj)):
                    Gbresult.objects.filter(IDcard=jg_obj[i]['IDcard']).update(rankingofCategory=i+1)
                # 直属单位排名
                zsdw_obj = Gbresult.objects.filter(category='直属单位').values('IDcard', 'score').order_by('score').reverse()
                for i in range(0, len(zsdw_obj)):
                    Gbresult.objects.filter(IDcard=zsdw_obj[i]['IDcard']).update(rankingofCategory=i+1)

                # 单位排名
                category = []
                category_obj = Gbresult.objects.values_list('department').distinct()
                for i in category_obj:
                    category.append(i[0])
                for i in category:
                    dep_obj = Gbresult.objects.filter(department=i).values('IDcard', 'score').order_by('score').reverse()
                    for j in range(0, len(dep_obj)):
                        Gbresult.objects.filter(IDcard=dep_obj[j]['IDcard']).update(rankingOfDep=j + 1)

                # 前百分之十,后百分之十
                total = len(gb_obj)  # 总人数
                top_ten = int(total*0.1)  # 前百分之十的最后一位
                last_ten = total - int(total * 0.1) + 1  # 后百分之十的第一位
                top_ten_score = Gbresult.objects.filter(rankingOfAll=top_ten).values('score')  # 前百分之十最后一名的分数
                last_ten_score = Gbresult.objects.filter(rankingOfAll=last_ten).values('score')  # 后百分之十第一名的分数
                for i in range(0, len(gb_obj)):
                    if gb_obj[i]['score'] >= top_ten_score[0]['score']:
                        Gbresult.objects.filter(IDcard=gb_obj[i]['IDcard']).update(TopTen=True)
                    if gb_obj[i]['score'] <= last_ten_score[0]['score']:
                        Gbresult.objects.filter(IDcard=gb_obj[i]['IDcard']).update(LastTen=True)

            ret.code = 205
            ret.data = '数据统计成功'
        except Exception as e:
            ret.code = 206
            ret.error = '数据统计失败'
            return Response(ret.dict)
        return Response(ret.dict)


class Bz_of_all(APIView):
    def get(self, request):
        """
        班子考核汇总表
        将两张班子考核结果表的数据汇总在一起，并计算排名
        """
        ret = BaseResponse()
        year = datetime.datetime.now().year  # 当前年份
        xy_obj = xybzResult.objects.values()  # 学院班子结果表
        zsdw_obj = zsdwbzResult.objects.values()  # 直属单位班子结果表

        try:
            with transaction.atomic():
                # 计算前，首先删除当前年份的数据
                Bzresult.objects.filter(year=year).all().delete()
                # 处理学院班子结果表
                for i in range(0, len(xy_obj)):
                    each_obj = BzTjInfo.objects.filter(number_id=xy_obj[i]['beiceping_id']).values('department_id')  # 单位名
                    # 将学院班子结果表的内容添加到班子结果汇总表中
                    Bzresult.objects.create(
                        beiceping=each_obj[0]['department_id'],
                        year=year,
                        index1=xy_obj[i]['index1'],
                        index2=xy_obj[i]['index2'],
                        index3=xy_obj[i]['index3'],
                        index4=xy_obj[i]['index4'],
                        index5=xy_obj[i]['index5'],
                        index6=xy_obj[i]['index6'],
                        index7=xy_obj[i]['index7'],
                        index8=xy_obj[i]['index8'],
                        index9=xy_obj[i]['index9'],
                        index10=xy_obj[i]['index10'],
                        index11=xy_obj[i]['index11'],
                        index12=xy_obj[i]['index12'],
                        score=xy_obj[i]['score']
                    )
                # 处理直属单位班子结果表
                for i in range(0, len(zsdw_obj)):
                    each_obj = BzTjInfo.objects.filter(number_id=zsdw_obj[i]['beiceping_id']).values('department_id')  # 单位名
                    # 将直属单位班子结果表内容添加到班子结果汇总表中
                    Bzresult.objects.create(
                        beiceping=each_obj[0]['department_id'],
                        year=year,
                        index1=zsdw_obj[i]['index1'],
                        index2=zsdw_obj[i]['index2'],
                        index3=zsdw_obj[i]['index3'],
                        index4=zsdw_obj[i]['index4'],
                        index5=zsdw_obj[i]['index5'],
                        index6=zsdw_obj[i]['index6'],
                        index7=zsdw_obj[i]['index7'],
                        index8=zsdw_obj[i]['index8'],
                        index9=zsdw_obj[i]['index9'],
                        index10=zsdw_obj[i]['index10'],
                        index11=zsdw_obj[i]['index11'],
                        index12=zsdw_obj[i]['index12'],
                        index19=zsdw_obj[i]['index19'],
                        index20=zsdw_obj[i]['index20'],
                        index21=zsdw_obj[i]['index21'],
                        score=zsdw_obj[i]['score']
                    )

                # 综合排名
                bz_obj = Bzresult.objects.values('beiceping', 'score').order_by('score').reverse()

                for i in range(0, len(bz_obj)):
                    Bzresult.objects.filter(beiceping=bz_obj[i]['beiceping']).update(rankingOfAll=i+1)

                # 前百分之十,后百分之十
                total = len(bz_obj)  # 总人数
                top_ten = int(total*0.1)  # 前百分之十的最后一位
                last_ten = total - int(total * 0.1) + 1  # 后百分之十的第一位
                top_ten_score = Bzresult.objects.filter(rankingOfAll=top_ten).values('score')  # 前百分之十最后一名的分数
                last_ten_score = Bzresult.objects.filter(rankingOfAll=last_ten).values('score')  # 后百分之十第一名的分数

                for i in range(0, len(bz_obj)):
                    if bz_obj[i]['score'] >= top_ten_score[0]['score']:
                        Bzresult.objects.filter(beiceping=bz_obj[i]['beiceping']).update(TopTen=True)
                    if bz_obj[i]['score'] <= last_ten_score[0]['score']:
                        Bzresult.objects.filter(beiceping=bz_obj[i]['beiceping']).update(LastTen=True)
        except Exception as e:
            ret.code = 206
            ret.error = '数据统计失败'
            return Response(ret.dict)

        ret.code = 205
        ret.data = '数据统计成功'
        return Response(ret.dict)