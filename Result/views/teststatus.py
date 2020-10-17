from Renyuan.models import Ceping
from Bumen.models import Department
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.base_response import BaseResponse


class LoadDep(APIView):
    def get(self, request):
        """
        点击考核结果查询的测评情况，会将各个单位加载出来
        :param request:
        :return:
        """
        ret = BaseResponse()
        department = request.GET.get('department')
        try:
            if department == 'xueyuan':
                dep = Department.objects.filter(category='学院').values('department')  # 学院单位名
            elif department == 'jiguan':
                dep = Department.objects.filter(category='机关').values('department')  # 机关单位名
            elif department == 'zhishudanwei':
                dep = Department.objects.filter(category='直属单位').values('department')  # 直属单位单位名
            ret.info = dep
        except Exception as e:
            pass
        return Response(ret.dict)


class CepingView(APIView):
    def post(self, request):
        """
        追踪测评情况,点击查询按钮
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        status_result = {}
        category = data['category']  # 学院、机关、直属单位
        department = data['department']  # 单位名
        try:
            if department:
                status_finish = Ceping.objects.filter(department__category=category, department=department, status=1).values('department_id', 'IDcard', 'name')
                status_unfinish = Ceping.objects.filter(department__category=category, department=department, status=0).values('department_id', 'IDcard', 'name')
            else:
                status_finish = Ceping.objects.filter(department__category=category, status=1).values('department_id', 'IDcard', 'name')
                status_unfinish = Ceping.objects.filter(department__category=category, status=0).values('department_id', 'IDcard', 'name')
            status_result['finish'] = status_finish
            status_result['unfinish'] = status_unfinish
        except Exception as e:
            ret.code = 202
            ret.error = '数据加载失败'
            return Response(ret.dict)
        ret.code = 201
        ret.data = '数据加载成功'
        ret.info = status_result
        return Response(ret.dict)