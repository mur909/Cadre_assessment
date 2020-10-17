from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ..serializers import UserSerializer
from utils.base_response import BaseResponse
from ..models import User, Role
from Bumen.models import Department
import uuid
import hashlib
from django.db import transaction

# Create your views here.


# class RegisterView(APIView):
#     def post(self, request):
#         """注册接口不展示"""
#         ser_obj = UserSerializer(data=request.data)
#         if ser_obj.is_valid():
#             ser_obj.save()
#             return Response('注册成功')
#         return Response(ser_obj.errors)
class Register1View(APIView):
    def post(self, request):
        """
        超级管理员注册接口
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        try:
            if data['username'] == '':
                ret.code = 113
                ret.data = '请输入用户名'
                return JsonResponse(ret.dict)
            if data['password'] == '':
                ret.code = 113
                ret.data = '请输入密码'
                return JsonResponse(ret.dict)
            if len(data['password']) < 6:
                ret.code = 114
                ret.data = '请设置密码长度不小于6'
                return JsonResponse(ret.dict)
            hash_pwd = hashlib.md5(data['password'].encode()).hexdigest()
            user_obj = User.objects.filter(username=data['username'])
            if user_obj:
                ret.code = 113
                ret.data = '当前用户名已存在'
                return JsonResponse(ret.dict)
            with transaction.atomic():
                User.objects.create(username=data['username'], password=hash_pwd, roles_id=1)
            ret.code = 111
            ret.data = '注册成功'
        except Exception as e:
            ret.code = 112
            ret.error = '注册失败'
            return JsonResponse(ret.dict)
        return JsonResponse(ret.dict)


class Register2View(APIView):
    def post(self, request):
        """
        二级管理员注册接口
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = request.data
        try:
            if data['username'] == '':
                ret.code = 113
                ret.data = '请输入用户名'
                return JsonResponse(ret.dict)
            if data['password'] == '':
                ret.code = 113
                ret.data = '请输入密码'
                return JsonResponse(ret.dict)
            if data['department__department'] == '':
                ret.code = 113
                ret.data = '请选择单位'
                return JsonResponse(ret.dict)
            if len(data['password']) < 6:
                ret.code = 114
                ret.data = '请设置密码长度不小于6'
                return JsonResponse(ret.dict)
            hash_pwd = hashlib.md5(data['password'].encode()).hexdigest()
            user_obj = User.objects.filter(username=data['username'])
            if user_obj:
                ret.code = 113
                ret.data = '当前用户名已存在'
                return JsonResponse(ret.dict)

            with transaction.atomic():
                dep = Department.objects.filter(department=data['department__department']).values()
                User.objects.create(
                    username=data['username'],
                    password=hash_pwd,
                    department_id=dep[0]['number'],
                    roles_id=2
                )
            ret.code = 111
            ret.data = '注册成功'
        except Exception as e:
            ret.code = 112
            ret.error = '注册失败'
            return JsonResponse(ret.dict)
        return JsonResponse(ret.dict)


class EditLowerAccount(APIView):
    def get(self, request):
        """
        删除二级管理员
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            id = request.GET.get('id')
            print(id)
            User.objects.filter(id=id).delete()
        except Exception as e:
            ret.code = 0
            ret.error = '删除失败'
            return Response(ret.dict)
        ret.code = 1
        ret.data = '删除成功'
        return Response(ret.dict)

    def post(self, request):
        """
        修改二级管理员
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            data = request.data
            id = data['id']
            username = data['username']
            password = data.get('password', None)
            if password:
                password = data['password']
                if len(password) < 6:
                    ret.code = 114
                    ret.data = '请设置密码长度不小于6'
                    return JsonResponse(ret.dict)
                hash_pwd = hashlib.md5(password.encode()).hexdigest()
            department = data['department__department']
            if username == '':
                ret.code = 113
                ret.data = '请输入用户名'
                return JsonResponse(ret.dict)
            with transaction.atomic():
                dep = Department.objects.filter(department=department).values()
                if password:
                    User.objects.filter(id=id).update(
                        username=username,
                        password=hash_pwd,
                        department_id=dep[0]['number'],
                    )
                else:
                    User.objects.filter(id=id).update(
                        username=username,
                        department_id=dep[0]['number'],
                    )
        except Exception as e:
            ret.code = 0
            ret.error = '修改失败'
            return JsonResponse(ret.dict)
        ret.code = 1
        ret.data = '修改成功'
        return JsonResponse(ret.dict)


class LoginView(APIView):
    def post(self, request):
        """
        登录接口
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = {}
        username = request.data.get('username')
        pwd = request.data.get('password')
        role = request.data.get('role')  # 超级管理员或者二级管理员
        hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
        try:
            user_obj = User.objects.filter(username=username, password=hash_pwd).first()
            if not user_obj:
                ret.code = 101
                ret.error = '用户名或密码错误'
                return JsonResponse(ret.dict)
            elif user_obj:
                if str(user_obj.roles) == role:
                    data['role'] = role
                    data['dep'] = str(user_obj.department)
                    # 登录成功
                    # 将权限信息写入到session
                    # 1.查当前登录用户拥有的权限
                    permission_list = User.objects.filter(username=username).values_list('roles__permissions__url').distinct()
                    # 2.将权限信息写入到session
                    request.session[settings.PERMISSION_SESSION_KEY] = list(permission_list)
                    request.session['cepingId'] = username
                    request.session['role'] = role  # 增加这个是为了只对二级管理员处理
                    if role == '二级管理员':
                        request.session['department'] = str(user_obj.department)
                    data['username'] = username
                    # 生成token
                    # user_obj.token = uuid.uuid4()
                    # user_obj.save()
                    ret.code = 103
                    ret.info = data
                    ret.data = '登录成功'
                else:
                    ret.code = 110
                    ret.data = '请选择正确的身份权限'
                    return JsonResponse(ret.dict)
        except Exception as e:
            ret.code = 102
            ret.error = '登录失败'
            return JsonResponse(ret.dict)
        return JsonResponse(ret.dict)


class AccountView(APIView):
    def get(self, request):
        """
        账户信息
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = {}
        try:
            dep = list(Department.objects.values('department', 'number'))
            super_ad = list(User.objects.filter(roles_id=1).values('username'))
            lower_ad = list(User.objects.filter(roles_id=2).values('id', 'username', 'department__department'))
            data['department'] = dep
            data['super'] = super_ad
            data['lower'] = lower_ad
            ret.code = 201
            ret.data = '数据加载成功'
            ret.info = data
        except Exception as e:
            ret.code = 202
            ret.data = '数据加载失败'
            return JsonResponse(ret.dict)
        return JsonResponse(ret.dict)
