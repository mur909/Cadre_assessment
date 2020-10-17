from rest_framework.response import Response
from rest_framework.views import APIView
from utils.base_response import BaseResponse
from Result.models import Gbresult, Bzresult
from Bumen.models import Department
import datetime


class Personal_report(APIView):
    def get(self, request):
        """
        干部返回前台数据
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = {}
        try:
            data['flag'] = [
                {'flag': '正处'},
                {'flag': '副处'}
            ]
            data['category'] = [
                {'category': '机关'},
                {'category': '学院'},
                {'category': '直属单位'},
            ]
            year_obj = Gbresult.objects.values('year').distinct()  # 返回年份
            data['year'] = year_obj

            xyDep_obj = Department.objects.filter(category='学院').values('department')
            for each in xyDep_obj:
                each['value'] = each['department']
                each['label'] = each['department']
            jgDep_obj = Department.objects.filter(category='机关').values('department')
            for each in jgDep_obj:
                each['value'] = each['department']
                each['label'] = each['department']
            zsdwDep_obj = Department.objects.filter(category='直属单位').values('department')
            for each in zsdwDep_obj:
                each['value'] = each['department']
                each['label'] = each['department']
            data['options'] = \
                [{
                    'value': 'jiguan',
                    'label': '机关',
                    'children': jgDep_obj
                }, {
                    'value': 'xueyuan',
                    'label': '学院（科研机构）',
                    'children': xyDep_obj
                }, {
                    'value': 'zhishudanwei',
                    'label': '直属单位',
                    'children': zsdwDep_obj
                }]

            tablename_obj = [
                {"name": "name", 'index': '姓名'},
                {"name": "IDcard", 'index': '一卡通'},
                {"name": "department", 'index': '单位'},
                {"name": "category", 'index': '单位类别'},
                {"name": "beiKaoHe", 'index': '标识'},
                {"name": "year", 'index': '年份'},
                {"name": "index1", 'index': '指标1'},
                {"name": "index2", 'index': '指标2'},
                {"name": "index3", 'index': '指标3'},
                {"name": "index4", 'index': '指标4'},
                {"name": "index5", 'index': '指标5'},
                {"name": "index6", 'index': '指标6'},
                {"name": "index7", 'index': '指标7'},
                {"name": "index8", 'index': '指标8'},
                {"name": "index9", 'index': '指标9'},
                {"name": "index10", 'index': '指标10'},
                {"name": "index11", 'index': '指标11'},
                {"name": "index12", 'index': '指标12'},
                {"name": "index13", 'index': '指标13'},
                {"name": "index14", 'index': '指标14'},
                {"name": "index15", 'index': '指标15'},
                {"name": "index16", 'index': '指标16'},
                {"name": "index17", 'index': '指标17'},
                {"name": "index18", 'index': '指标18'},
                {"name": "index19", 'index': '指标19'},
                {"name": "index20", 'index': '指标20'},
                {"name": "index21", 'index': '指标21'},
                {"name": "index22", 'index': '指标22'},
                {"name": "index23", 'index': '指标23'},
                {"name": "score", 'index': '分数'},
                {"name": "rankingOfLine", 'index': '条线排名'},
                {"name": "rankingOfDep", 'index': '本单位排名'},
                {"name": "rankingofCategory", 'index': '所属机构排名'},
                {"name": "rankingOfAll", 'index': '全校排名'},
                {"name": "TopTen", 'index': '前10%'},
                {"name": "LastTen", 'index': '后10%'},
                {"name": "Excellent", 'index': '优秀'}
            ]
            data['tablename'] = tablename_obj
            ret.info = data
        except Exception as e:
            pass
        return Response(ret.dict)

    def post(self, request):
        """
        干部or个人考核结果报表
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        condition = {}
        conditions = {}
        is_dep = 0
        try:
            year = data['year']  # 年份(前台默认传过来当前年份)
            name = data['name']  # 姓名
            department = data.get('department', None)
            if department:
                department = data['department']  # 单位
            category = data['category']  # 类别
            flag = data['flag']  # 标识
            if name:
                condition['name__icontains'] = name
                conditions['name__icontains'] = name
            if department:
                condition['department'] = department
                is_dep = 1
            if flag:
                condition['beiKaoHe__contains'] = flag
                conditions['beiKaoHe__contains'] = flag
            if year:
                condition['year'] = year
                conditions['year'] = year
            elif not year:
                year = datetime.datetime.now().year  # 当前年份
                condition['year'] = year
                conditions['year'] = year

            if category:
                conditions['category'] = category
                obj = Gbresult.objects.filter(**conditions).values().order_by('rankingofCategory')
            elif category == '' and is_dep == 1:
                obj = Gbresult.objects.filter(**condition).values().order_by('rankingOfDep')
            elif category == '' and is_dep == 0:
                obj = Gbresult.objects.filter(**condition).values().order_by('rankingOfAll')

            if not obj:
                table = {}
                tables = []
                verbosename = Gbresult._meta.fields  # 获取被导入数据库的字段
                for name in verbosename:
                    table['{}'.format(name.name)] = ''
                tables.append(table)
                ret.code = 201
                ret.data = '没有对应内容'
                ret.info = tables
                return Response(ret.dict)
            ret.code = 201
            ret.data = '数据加载成功'
            ret.info = obj
        except Exception as e:
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        return Response(ret.dict)

    def put(self, request):
        """
        编辑是否为年终考核优秀
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            idcard = request.GET.get('id')  # 被测评用户id
            is_excellent = request.GET.get('status')  # 是否优秀标志：0/1
            Excellent = Gbresult.objects.filter(IDcard=idcard).values('Excellent')[0]
            if Excellent['Excellent']:
                if int(is_excellent):
                    ret.code = 209
                    ret.data = '状态未改变'
                    return Response(ret.dict)
                else:
                    Gbresult.objects.filter(IDcard=idcard).update(Excellent=is_excellent)
            else:
                if int(is_excellent):
                    Gbresult.objects.filter(IDcard=idcard).update(Excellent=is_excellent)
                else:
                    ret.code = 209
                    ret.data = '状态未改变'
                    return Response(ret.dict)
            ret.code = 305
            ret.data = '修改成功'
        except Exception as e:
            ret.code = 306
            ret.error = '修改失败'
            return Response(ret.dict)
        return Response(ret.dict)


class Banzi_report(APIView):
    def get(self, request):
        """
        班子返回前台数据
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = {}
        try:
            year_obj = Bzresult.objects.values('year').distinct()  # 返回年份
            xyDep_obj = Department.objects.filter(category='学院').values('department')
            for each in xyDep_obj:
                each['value'] = each['department']
                each['label'] = each['department']
            zsdwDep_obj = Department.objects.filter(category='直属单位').values('department')
            for each in zsdwDep_obj:
                each['value'] = each['department']
                each['label'] = each['department']
            data['options'] = \
                [{
                    'value': 'xueyuan',
                    'label': '学院',
                    'children': xyDep_obj
                }, {
                    'value': 'zhishudanwei',
                    'label': '直属单位',
                    'children': zsdwDep_obj
                }]
            tablename_obj = [
                {"name": "beiceping", 'index': '单位名'},
                {"name": "year", 'index': '年份'},
                {"name": "index1", 'index': '指标1'},
                {"name": "index2", 'index': '指标2'},
                {"name": "index3", 'index': '指标3'},
                {"name": "index4", 'index': '指标4'},
                {"name": "index5", 'index': '指标5'},
                {"name": "index6", 'index': '指标6'},
                {"name": "index7", 'index': '指标7'},
                {"name": "index8", 'index': '指标8'},
                {"name": "index9", 'index': '指标9'},
                {"name": "index10", 'index': '指标10'},
                {"name": "index11", 'index': '指标11'},
                {"name": "index12", 'index': '指标12'},
                {"name": "index19", 'index': '指标19'},
                {"name": "index20", 'index': '指标20'},
                {"name": "index21", 'index': '指标21'},
                {"name": "score", 'index': '分数'},
                {"name": "rankingOfLine", 'index': '条线排名'},
                {"name": "rankingOfAll", 'index': '全校排名'},
                {"name": "TopTen", 'index': '前10%'},
                {"name": "LastTen", 'index': '后10%'},
                {"name": "Excellent", 'index': '优秀'}
            ]
            data['year'] = year_obj
            data['tablename'] = tablename_obj
            ret.info = data
        except Exception as e:
            pass
        return Response(ret.dict)

    def post(self, request):
        """
        班子考核结果报表
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        try:
            year = data['year']  # 年份(前台默认传过来当前年份)
            beiceping = data.get('beiceping', None)
            if beiceping:
                beiceping = data['beiceping']  # 单位
            if not year:
                year = datetime.datetime.now().year  # 当前年份
            if beiceping:
                obj = Bzresult.objects.filter(year=year, beiceping=beiceping).values()
            else:
                obj = Bzresult.objects.filter(year=year).values().order_by('rankingOfAll')

            if not obj:
                ret.code = 208
                ret.data = '没有对应内容'
                return Response(ret.dict)
            ret.code = 201
            ret.data = '数据加载成功'
            ret.info = obj
        except Exception as e:
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        return Response(ret.dict)

    def put(self, request):
        """
        编辑是否为年终考核优秀
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            beiceping = request.GET.get('beiceping')  # 被测评单位
            is_excellent = request.GET.get('status')  # 是否优秀标志：0/1
            Excellent = Bzresult.objects.filter(beiceping=beiceping).values('Excellent')[0]
            if Excellent['Excellent']:
                if int(is_excellent):
                    ret.code = 209
                    ret.data = '状态未改变'
                    return Response(ret.dict)
                else:
                    Bzresult.objects.filter(beiceping=beiceping).update(Excellent=is_excellent)
            else:
                if int(is_excellent):
                    Bzresult.objects.filter(beiceping=beiceping).update(Excellent=is_excellent)
                else:
                    ret.code = 209
                    ret.data = '状态未改变'
                    return Response(ret.dict)
            ret.code = 305
            ret.data = '修改成功'
        except Exception as e:
            ret.code = 306
            ret.error = '修改失败'
            return Response(ret.dict)
        return Response(ret.dict)