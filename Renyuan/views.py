from django.http import JsonResponse
from .models import Ceping, Beiceping
from Bumen.models import Department
from Renyuan.models import Zhiwu, SpecialStatus
from Zhiwei.models import Rank
from Fangan.models import BzTjInfo
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from utils.base_response import BaseResponse


# 显示所有被测评人员
def get_beicepings(request):
    try:
        obj_beicepings = Beiceping.objects.all().values()
        beicepings = list(obj_beicepings)
        return JsonResponse({'code': 1, 'data': beicepings})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "获取被测评信息出现异常，具体错误：" + str(e)})


# 显示所有测评人员， 二级管理员可操作
def get_cepings(request):
    try:
        department = request.session.get('department', None)
        if department is None:
            obj_cepings = Ceping.objects.all().values()
        else:
            obj_cepings = Ceping.objects.filter(department_id=department).all().values()
        cepings = list(obj_cepings)
        return JsonResponse({'code': 1, 'data': cepings})
    except Exception as e:
        return JsonResponse({'code': 0, 'data': "获取测评信息出现异常，具体错误：" + str(e)})


# 测评人修改， 二级管理员可操作
class EditCeping(APIView):
    def get(self, request):
        """
        点击测评人中的修改
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            # 单位
            department = Department.objects.values('department')
            for each in department:
                each['value'] = each['department']
            # 职务
            zhiwu = Zhiwu.objects.values('name')
            for each in zhiwu:
                each['value'] = each['name']
            # 职级
            rank = Rank.objects.values('rank', 'number')
            # 岗位
            post = BzTjInfo.objects.values('department', 'number')
            # 特殊人员身份
            special = SpecialStatus.objects.values('name', 'code')
            condition = {
                'department': department,
                'zhiwu': zhiwu,
                'rank': rank,
                'post': post,
                'special': special,
                'status': [
                    {'label': '已测评', 'value': 1},
                    {'label': '未测评', 'value': 0},
                ]
            }
            ret.info = condition
            return Response(ret.dict)
        except Exception as e:
            pass


# 被测评人修改
class EditBeiCeping(APIView):
    def get(self, request):
        """
        点击被测评人中的修改
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            # 单位
            department = Department.objects.values('department')
            for each in department:
                each['value'] = each['department']
            # 职务
            zhiwu = Zhiwu.objects.filter(id__in=[2, 3, 4, 5]).values('name')
            for each in zhiwu:
                each['value'] = each['name']
            # 职级
            rank = Rank.objects.values('rank', 'number')
            condition = {
                'department': department,
                'zhiwu': zhiwu,
                'rank': rank
            }
            ret.info = condition
            return Response(ret.dict)
        except Exception as e:
            pass


# 查询被测评人员的信息
def query_beiceping(request):
    """接收前端传递过来的值"""
    data = json.loads(request.body.decode('utf-8'))
    try:
        # 使用ORM获取满足条件的干部信息，并把对象转为字典格式
        obj_beiceping = Beiceping.objects.filter(
            Q(name__icontains=data['inputstr'])
            | Q(IDcard__icontains=data['inputstr'])
            | Q(post__icontains=data['inputstr'])
            | Q(post_id__icontains=data['inputstr'])
            | Q(department_type__icontains=data['inputstr'])
            | Q(beiKaoHe__icontains=data['inputstr'])
            | Q(cePing__icontains=data['inputstr'])
            | Q(department__department__icontains=data['inputstr'])
            | Q(department_num__number__icontains=data['inputstr'])
            | Q(rank_id__number__icontains=data['inputstr'])
        ).values()

        """把结果转为list类型"""
        beiceping = list(obj_beiceping)
        """返回Json格式"""
        return JsonResponse({'code': 1, 'data': beiceping})
    except Exception as e:
        """如果出现异常，返回异常消息"""
        return JsonResponse({'code': 0, 'msg': "查询被测评信息出现异常，具体错误：" + str(e)})


# 添加被测评人员到数据库
class add_beiceping(APIView):
    def post(self, request):
        """接受前端传递过来的值"""
        data = json.loads(request.body.decode("utf-8"))
        try:
            """添加到数据库"""
            obj_beiceping = Beiceping(
                name=data['name'],
                IDcard=data['IDcard'],
                post=data['post'],
                post_id=data['post_id'],
                department_id=data['department_id'],
                department_num_id=data['department_num_id'],
                rank_id_id=data['rank_id_id'],
                department_type=data['department_type'],
                beiKaoHe=data['beiKaoHe'],
                # EvaluationIndex=data['EvaluationIndex'],
                cePing=data['cePing']
            )
            """执行添加"""
            obj_beiceping.save()
            """使用ORM获取所有被测评人员的信息，并把对象转为字典格式"""
            obj_beiceping = Beiceping.objects.all().values()
            """把外层的容器转为List"""
            beiceping = list(obj_beiceping)
            """返回"""
            return JsonResponse({'code': 1, 'data': beiceping})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "添加被测评人员出现异常，具体原因：" + str(e)})


# 修改被测评人员到数据库
class update_beiceping(APIView):
    def post(self, request):
        """接受前端传递过来的值"""
        data = json.loads(request.body.decode("utf-8"))
        try:
            bcp_obj = Beiceping.objects.filter(IDcard=data['IDcard']).values('department_id')
            if data['department_id'] != bcp_obj[0]['department_id']:
                dep_obj = Department.objects.filter(department=data['department_id']).values('number', 'category')
            else:
                dep_obj = False
            obj_beiceping = Beiceping.objects.get(IDcard=data['IDcard'])
            # 依次修改
            obj_beiceping.name = data['name']
            obj_beiceping.IDcard = data['IDcard']
            obj_beiceping.post = data['post']
            obj_beiceping.post_id = data['post_id']
            obj_beiceping.department_type = (dep_obj[0]['category'] if dep_obj else data['department_type'])
            obj_beiceping.beiKaoHe = data['beiKaoHe']
            obj_beiceping.cePing = data['cePing']
            obj_beiceping.department_id = data['department_id']
            obj_beiceping.department_num_id = (dep_obj[0]['number'] if dep_obj else data['department_num_id'])
            obj_beiceping.rank_id_id = data['rank_id_id']
            """执行添加"""
            obj_beiceping.save()
            """使用ORM获取所有被测评人员的信息，并把对象转为字典格式"""
            obj_beiceping = Beiceping.objects.all().values()
            """把外层的容器转为List"""
            beiceping = list(obj_beiceping)
            """返回"""
            return JsonResponse({'code': 1, 'data': beiceping})
        except Exception as e:
            print(e)
            return JsonResponse({'code': 0, 'msg': "修改被测评人员信息出现异常，具体原因：" + str(e)})


# 删除一条被测评人员信息
def delete_a_beiceping(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        """根据IDcard删除指定信息"""
        obj_beiceping = Beiceping.objects.get(IDcard=data['IDcard'])
        """执行删除"""
        obj_beiceping.delete()
        """使用ORM获取所有被测评人员信息"""
        obj_Beicepings = Beiceping.objects.all().values()
        """把结果转为list类型"""
        beiceping = list(obj_Beicepings)
        return JsonResponse({'code': 1, 'data': beiceping})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '删除被测评人员信息出现异常，具体原因：' + str(e)})


# 批量删除被测评人员信息
def delete_beicepings(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        for one_beiceping in data['Bcepings']:
            """查询当前记录"""
            obj_beiceping = Beiceping.objects.get(IDcard=one_beiceping['IDcard'])
            """执行删除"""
            obj_beiceping.delete()
        """使用ORM获取所有学生信息"""
        beicepings = Beiceping.objects.all().values()
        """把结果转为list类型"""
        Beicepings = list(beicepings)
        """返回Json格式"""
        return JsonResponse({'code': 1, 'data': Beicepings})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "批量删除被测评人员信息写入数据库出现异常，具体原因：" + str(e)})


# 查询测评人员信息
def query_ceping(request):
    """接收前端传递过来的值"""
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_ceping = Ceping.objects.filter(
            Q(name__icontains=data['inputstr']) |
            Q(IDcard__icontains=data['inputstr']) |
            Q(identity__icontains=data['inputstr']) |
            Q(zhiwu__icontains=data['inputstr']) |
            Q(special_identity__icontains=data['inputstr']) |
            Q(cePing__icontains=data['inputstr']) |
            Q(status__icontains=data['inputstr'])
        ).values()

        """把结果转为list类型"""
        ceping = list(obj_ceping)
        """返回Json格式"""
        return JsonResponse({'code': 1, 'data': ceping})
    except Exception as e:
        print(e)
        """如果出现异常，返回异常消息"""
        return JsonResponse({'code': 0, 'msg': "查询测评信息出现异常，具体错误：" + str(e)})


# 添加测评人员信息， 二级管理员可操作
class add_ceping(APIView):
    def post(self, request):
        """接受前端传递过来的值"""
        data = json.loads(request.body.decode("utf-8"))
        try:
            """添加到数据库"""
            obj_ceping = Ceping(
                name=data['name'],
                IDcard=data['IDcard'],
                password=data['password'],
                identity=data['identity'],
                zhiwu=data['zhiwu'],
                special_identity=data['special_identity'],
                cePing=data['cePing'],
                ganBu_unfinished=data['ganBu_unfinished'],
                ganBu_finished=data['ganBu_finished'],
                banZi_unfinished=data['banZi_unfinished'],
                banZi_finished=data['banZi_finished'],
                status=data['status'],
                department_id=data['department_id'],
                post_id_id=data['post_id_id'],
                rank_id_id=data['rank_id_id']
            )
            """执行添加"""
            obj_ceping.save()
            """使用ORM获取所有测评人员的信息，并把对象转为字典格式"""
            obj_ceping = Ceping.objects.all().values()
            """把外层的容器转为List"""
            ceping = list(obj_ceping)
            """返回"""
            return JsonResponse({'code': 1, 'data': ceping})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "添加测评人员出现异常，具体原因：" + str(e)})


# 修改测评人员到数据库， 二级管理员可操作
class update_ceping(APIView):
    def post(self, request):
        """接受前端传递过来的值"""
        data = json.loads(request.body.decode("utf-8"))
        dep = 0
        try:
            cp_obj = Ceping.objects.filter(IDcard=data['IDcard']).values('department_id')
            if data['department_id'] != cp_obj[0]['department_id']:
                dep_obj = Department.objects.filter(department=data['department_id']).values('category')
                if dep_obj[0]['category'] == '机关':
                    dep = 1
                elif dep_obj[0]['category'] == '学院':
                    dep = 2
                elif dep_obj[0]['category'] == '直属单位':
                    dep = 3
            if len(data['special_identity']) == 0:
                special_identity = ''
            else:
                special_identity = ''
                for each in range(0, len(data['special_identity'])):
                    special_identity = special_identity + data['special_identity'][each]
            obj_ceping = Ceping.objects.get(IDcard=data['IDcard'])
            # 依次修改
            obj_ceping.name = data['name']
            obj_ceping.IDcard = data['IDcard']
            obj_ceping.password = data['password']
            obj_ceping.identity = (dep if dep is not 0 else data['identity'])
            obj_ceping.zhiwu = data['zhiwu']
            obj_ceping.special_identity = special_identity
            obj_ceping.cePing = data['cePing']
            obj_ceping.ganBu_finished = data['ganBu_finished']
            obj_ceping.ganBu_unfinished = data['ganBu_unfinished']
            obj_ceping.banZi_finished = data['banZi_finished']
            obj_ceping.banZi_unfinished = data['banZi_unfinished']
            obj_ceping.status = data['status']
            obj_ceping.department_id = data['department_id']
            obj_ceping.post_id_id = data['post_id_id']
            obj_ceping.rank_id_id = data['rank_id_id']
            """执行添加"""
            obj_ceping.save()
            """使用ORM获取所有测评人员的信息，并把对象转为字典格式"""
            obj_ceping = Ceping.objects.all().values()
            """把外层的容器转为List"""
            beiceping = list(obj_ceping)
            """返回"""
            return JsonResponse({'code': 1, 'data': beiceping})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "修改测评人员信息出现异常，具体原因：" + str(e)})


# 删除一条测评人员信息， 二级管理员可操作
def delete_a_ceping(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        """根据IDcard删除指定信息"""
        obj_ceping = Ceping.objects.get(IDcard=data['IDcard'])
        """执行删除"""
        obj_ceping.delete()
        """使用ORM获取所有测评人员信息"""
        obj_cepings = Ceping.objects.all().values()
        """把结果转为list类型"""
        ceping = list(obj_cepings)
        return JsonResponse({'code': 1, 'data': ceping})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '删除测评人员信息出现异常，具体原因：' + str(e)})


# 批量删除测评人员信息， 二级管理员可操作
def delete_cepings(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        for one_ceping in data['Cepings']:
            """查询当前记录"""
            obj_ceping = Ceping.objects.get(IDcard=one_ceping['IDcard'])
            """执行删除"""
            obj_ceping.delete()
        """使用ORM获取所有测评人员信息"""
        cepings = Ceping.objects.all().values()
        """把结果转为list类型"""
        cepings = list(cepings)
        """返回Json格式"""
        return JsonResponse({'code': 1, 'data': cepings})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "批量删除测评人员信息写入数据库出现异常，具体原因：" + str(e)})
