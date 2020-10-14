from rest_framework.response import Response
from rest_framework.views import APIView
from utils.base_response import BaseResponse
from Bumen.models import Department
from Renyuan.models import Beiceping
from Fangan.models import jggbIndexWeight, xygbIndexWeight, zsdwgbIndexWeight, GbCpWeight, BzCpWeight, \
    xygbResult, jggbResult, zsdwgbResult, \
    xybzIndexWeight, zsdwbzIndexWeight, xybzResult, zsdwbzResult


class GanbuView(APIView):
    def get(self, request):
        """
        点击考核结果查询，点击干部按钮，会将各种查询条件反馈到前台
        :param request:
        :return:
        """
        ret = BaseResponse()
        condition = {}  # 存储各种条件
        name = [{'name': '被测评人', 'index': 'beiceping_id__name'}, {'name': '职级', 'index': 'level'},
                {'name': '单位名', 'index': 'depNum_id__department'}, {'name': '职务', 'index': 'zhiwu'},
                {'name': '人数', 'index': 'count'}, {'name': '得分', 'index': 'score'}]
        department = request.GET.get('department')
        try:
            if department == 'xueyuan':
                dep = Department.objects.filter(category='学院').values('department')  # 学院单位名
                index = xygbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values(
                    'index')  # 学院干部指标
                # 返回生成表格的表头
                index19 = GbCpWeight.objects.filter(code='001').values_list('name', flat=True)[0]  # 学院校领导
                index20 = GbCpWeight.objects.filter(code='002').values_list('name', flat=True)[0]  # 班子成员
                index21 = GbCpWeight.objects.filter(code='003').values_list('name', flat=True)[0]  # 学院师生
                index22 = GbCpWeight.objects.filter(code='004').values_list('name', flat=True)[0]  # 对口机关
                for i in range(0, len(index)):
                    name.append({'name': '{}'.format(index[i]['index']), 'index': 'index{}'.format(i+1)})
                name.append({'name': '{}'.format(index19), 'index': 'index19'})
                name.append({'name': '{}'.format(index20), 'index': 'index20'})
                name.append({'name': '{}'.format(index21), 'index': 'index21'})
                name.append({'name': '{}'.format(index22), 'index': 'index22'})

            elif department == 'jiguan':
                dep = Department.objects.filter(category='机关').values('department')  # 机关单位名
                index = jggbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values(
                    'index')  # 机关干部指标

                index19 = GbCpWeight.objects.filter(code='005').values_list('name', flat=True)[0]  # 机关校领导权重
                index20 = GbCpWeight.objects.filter(code='006').values_list('name', flat=True)[0]  # 党政处级权重
                index21 = GbCpWeight.objects.filter(code='007').values_list('name', flat=True)[0]  # 党政科级及职工权重
                index22 = GbCpWeight.objects.filter(code='008').values_list('name', flat=True)[0]  # 学院领导权重
                index23 = GbCpWeight.objects.filter(code='009').values_list('name', flat=True)[0]  # 学院相关权重
                for i in range(0, len(index)):
                    name.append({'name': '{}'.format(index[i]['index']), 'index': 'index{}'.format(i+1)})
                name.append({'name': '{}'.format(index19), 'index': 'index19'})
                name.append({'name': '{}'.format(index20), 'index': 'index20'})
                name.append({'name': '{}'.format(index21), 'index': 'index21'})
                name.append({'name': '{}'.format(index22), 'index': 'index22'})
                name.append({'name': '{}'.format(index23), 'index': 'index23'})

            elif department == 'zhishudanwei':
                dep = Department.objects.filter(category='直属单位').values('department')  # 直属单位单位名
                index = zsdwgbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values(
                    'index')  # 直属单位干部指标

                index19 = GbCpWeight.objects.filter(code='010').values_list('name', flat=True)[0]  # 直属单位校领导权重
                index20 = GbCpWeight.objects.filter(code='011').values_list('name', flat=True)[0]  # 单位班子权重
                index21 = GbCpWeight.objects.filter(code='012').values_list('name', flat=True)[0]  # 相关人员权重
                index22 = GbCpWeight.objects.filter(code='013').values_list('name', flat=True)[0]  # 直属单位学院领导权重
                index23 = GbCpWeight.objects.filter(code='014').values_list('name', flat=True)[0]  # 直属单位学院相关权重
                for i in range(0, len(index)):
                    name.append({'name': '{}'.format(index[i]['index']), 'index': 'index{}'.format(i+1)})
                name.append({'name': '{}'.format(index19), 'index': 'index19'})
                name.append({'name': '{}'.format(index20), 'index': 'index20'})
                name.append({'name': '{}'.format(index21), 'index': 'index21'})
                name.append({'name': '{}'.format(index22), 'index': 'index22'})
                name.append({'name': '{}'.format(index23), 'index': 'index23'})

            for i in range(0, len(index)):
                index[i]['id'] = 'index{}'.format(i + 1)
            zhiwu = Beiceping.objects.values('beiKaoHe').distinct()  # 职务
            rank = [{'rank': '上级'}, {'rank': '同级'}, {'rank': '下级'}, {'rank': '全体'}]  # 级别关系
            condition['dep'] = dep
            condition['zhiwu'] = zhiwu
            condition['rank'] = rank
            condition['index'] = index
            condition['table_name'] = name
            ret.info = condition
        except Exception as e:
            pass
        return Response(ret.dict)


class BanziView(APIView):
    def get(self, request):
        """
        点击考核结果查询，点击班子按钮，会将各种查询条件反馈到前台
        :param request:
        :return:
        """
        ret = BaseResponse()
        condition = {}  # 存储各种条件
        name = [{'name': '被测评单位', 'index': 'beiceping_id__department'}, {'name': '人数', 'index': 'count'},
                {'name': '得分', 'index': 'score'}]
        department = request.GET.get('department')
        try:
            if department == 'xueyuan':
                dep = Department.objects.filter(category='学院').values('department')  # 单位名
                index = xybzIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values(
                    'index')  # 学院班子指标
                for i in range(0, len(index)):
                    name.append({'name': '{}'.format(index[i]['index']), 'index': 'index{}'.format(i+1)})
            elif department == 'zhishudanwei':
                dep = Department.objects.filter(category='直属单位').values('department')  # 单位名
                index = zsdwbzIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values(
                    'index')  # 直属单位班子指标
                index19 = BzCpWeight.objects.filter(code='001').values_list('name', flat=True)[0]  # 校领导权重
                index20 = BzCpWeight.objects.filter(code='002').values_list('name', flat=True)[0]  # 党政负责人权重
                index21 = BzCpWeight.objects.filter(code='003').values_list('name', flat=True)[0]  # 单位职工师生代表权重
                for i in range(0, len(index)):
                    name.append({'name': '{}'.format(index[i]['index']), 'index': 'index{}'.format(i+1)})
                name.append({'name': '{}'.format(index19), 'index': 'index19'})
                name.append({'name': '{}'.format(index20), 'index': 'index20'})
                name.append({'name': '{}'.format(index21), 'index': 'index21'})
            for i in range(0, len(index)):
                index[i]['id'] = 'index{}'.format(i + 1)
            condition['dep'] = dep
            condition['index'] = index
            condition['table_name'] = name
            ret.info = condition
        except Exception as e:
            pass
        return Response(ret.dict)


class GbSearchView(APIView):
    def post(self, request):
        """
        结果表查询
        干部条件搜索
        :param request:
        :return:
        """
        ret = BaseResponse()
        condition = {}  # 存储filter条件
        id_lst = []  # 存储人员ID
        data = request.data
        try:
            category = data['category']  # 分类
            department = data['department']  # 单位
            zhiwu = data['zhiwu']  # 职务
            level = data['level']  # 职级
            name = data['name']  # 姓名
            index = data['index']  # 指标
            if department:
                dep_num = Department.objects.filter(department=department).values_list('number', flat=True)[0]  # 单位名
                condition['depNum_id'] = dep_num  # 单位名
            if zhiwu:
                condition['zhiwu'] = zhiwu  # 职务
            if level:
                condition['level'] = level  # 级别关系
            if name:
                beiceping_id = Beiceping.objects.filter(name__contains=name).values_list('IDcard')
                for i in range(0, len(beiceping_id)):
                    id_lst.append(beiceping_id[i][0])
                condition['beiceping_id__in'] = id_lst  # 人员列表

            if category == 'xueyuan':
                lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score', 'index19',
                       'index20', 'index21', 'index22']
                for i in index:
                    lst.append(i)
                result = xygbResult.objects.filter(**condition).values(*lst)
                if len(condition) == 0:
                    lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score',
                           'index1', 'index2', 'index3', 'index4', 'index5', 'index6', 'index7', 'index8', 'index9',
                           'index10', 'index11', 'index12', 'index13', 'index14', 'index15', 'index16', 'index17',
                           'index18',  'index19',
                           'index20', 'index21', 'index22']
                    result = xygbResult.objects.values(*lst)
            elif category == 'jiguan':
                lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score', 'index19',
                       'index20', 'index21', 'index22', 'index23']
                for i in index:
                    lst.append(i)
                result = jggbResult.objects.filter(**condition).values(*lst)
                if len(condition) == 0:
                    lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score',
                           'index1', 'index2', 'index3', 'index4', 'index5', 'index6', 'index7', 'index8', 'index9',
                           'index10', 'index11', 'index12', 'index13', 'index14', 'index15', 'index16', 'index17',
                           'index18',  'index19', 'index20', 'index21', 'index22', 'index23']
                    result = jggbResult.objects.values(*lst)
            elif category == 'zhishudanwei':
                lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score', 'index19',
                       'index20', 'index21', 'index22', 'index23']
                for i in index:
                    lst.append(i)
                result = zsdwgbResult.objects.filter(**condition).values(*lst)
                if len(condition) == 0:
                    lst = ['beiceping_id__name', 'level', 'depNum_id__department', 'zhiwu', 'count', 'score',
                           'index1', 'index2', 'index3', 'index4', 'index5', 'index6', 'index7', 'index8', 'index9',
                           'index10', 'index11', 'index12', 'index13', 'index14', 'index15', 'index16', 'index17',
                           'index18',  'index19', 'index20', 'index21', 'index22', 'index23']
                    result = zsdwgbResult.objects.values(*lst)
            ret.info = result
            # if len(condition) == 0:
            #     ret.code = 207
            #     ret.data = '请输入查询条件'
            #     return Response(ret.dict)
            ret.code = 201
            ret.data = '数据加载成功'
        except Exception as e:
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        return Response(ret.dict)


class BzSearchView(APIView):
    def post(self, request):
        """
        结果表查询
        班子条件搜索
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        try:
            category = data['category']  # 分类
            department = data['department']  # 单位
            index = data['index']  # 指标
            # if not department:
            #     ret.code = 207
            #     ret.data = '请输入查询条件'
            #     return Response(ret.dict)
            if department:
                dep_num = Department.objects.filter(department=department).values_list('number', flat=True)[0]
            if category == 'xueyuan':
                if not department:
                    lst = ['beiceping_id__department', 'count', 'score', 'index1', 'index2', 'index3', 'index4',
                           'index5', 'index6', 'index7', 'index8', 'index9', 'index10', 'index11', 'index12']
                    result = xybzResult.objects.values(*lst)
                else:
                    lst = ['beiceping_id__department', 'count', 'score']
                    for i in index:
                        lst.append(i)
                    result = xybzResult.objects.filter(beiceping_id=dep_num).values(*lst)
            elif category == 'zhishudanwei':
                if not department:
                    lst = ['beiceping_id__department', 'count', 'score', 'index1', 'index2', 'index3', 'index4',
                           'index5', 'index6', 'index7', 'index8', 'index9', 'index10', 'index11', 'index12', 'index19',
                           'index20', 'index21']
                    result = zsdwbzResult.objects.values(*lst)
                else:
                    lst = ['beiceping_id__department', 'count', 'score', 'index19', 'index20', 'index21']
                    for i in index:
                        lst.append(i)
                    result = zsdwbzResult.objects.filter(beiceping_id=dep_num).values(*lst)
            ret.info = result

            ret.code = 201
            ret.data = '数据加载成功'
        except Exception as e:
            print(e)
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        return Response(ret.dict)


class LineView(APIView):
    def post(self, request):
        """
        生成折线图
        :param request:
        :return:
        """
        ret = BaseResponse()
        recieve = request.data
        data = []
        try:
            result = recieve['result']  # 结果
            category = recieve['category']  # 分类
            department = recieve['department']  # 单位
            index = recieve['index']  # 指标

            if category == 'xueyuan':
                lst = []
                for i in index:
                    index_name = xygbIndexWeight.objects.filter(code='00{}'.format(i[5:])).values_list('index', flat=True)[0]
                    lst.append(str(index_name))
            elif category == 'jiguan':
                lst = []
                for i in index:
                    index_name = jggbIndexWeight.objects.filter(code='00{}'.format(i[5:])).values_list('index', flat=True)[0]
                    lst.append(index_name)
            elif category == 'zhishudanwei':
                lst = []
                for i in index:
                    index_name = zsdwgbIndexWeight.objects.filter(code='00{}'.format(i[5:])).values_list('index', flat=True)[0]
                    lst.append(index_name)

            for i in result:
                score = []
                for index_id in index:
                    if i.get(index_id, None):
                        score.append(i[index_id])
                data.append({'label': i['beiceping_id__name'], 'data': score})
            options = {
                'type': 'line',
                'title': {
                    'text': department
                },
                'bgColor': '#fbfbfb',
                'labels': lst,
                'datasets': data
            }
            ret.code = 201
            ret.data = '数据加载成功'
            ret.info = options
        except Exception as e:
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        return Response(ret.dict)