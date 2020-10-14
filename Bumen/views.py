from django.shortcuts import render
from django.views import View
import json
from rest_framework.views import APIView
from utils.base_response import BaseResponse
from Bumen.models import Department
from Fangan.models import BzTjInfo
from django.http import JsonResponse


class ReturnInfo(APIView):
    def get(self, request):
        """
        返回班子信息
        :param request:
        :return:
        """
        ret = BaseResponse()
        data = {}
        try:
            data['tableName'] = [
                {'index': 'department_id', 'name': '被测评单位'},
                {'index': 'number_id', 'name': '单位名'},
                {'index': 'type', 'name': '类别'},
                {'index': 'cePing', 'name': '是否测评'},
            ]
            obj = BzTjInfo.objects.values()
            data['obj'] = list(obj)
        except Exception as e:
            ret.code = 0
            ret.error = '加载失败'
            return JsonResponse(ret.dict)
        ret.code = 1
        ret.data = '加载成功'
        ret.info = data
        return JsonResponse(ret.dict)


class GenerateBz(APIView):
    def get(self, request):
        """
        根据单位表，自动生成领导班子统计信息表
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            department_obj = Department.objects.values()  # 获取单位表所有对象
            BzTjInfo.objects.all().delete()  # 首先清空领导班子统计信息表
            for each_obj in department_obj:
                print(each_obj)
                BzTjInfo.objects.create(
                    id=each_obj['id'],
                    department_id=each_obj['department'],
                    number_id=each_obj['number'],
                    type=each_obj['category'],
                    cePing=1
                )
        except Exception as e:
            ret.code = 202
            ret.error = '数据生成失败'
            return JsonResponse(ret.dict)
        ret.code = 201
        ret.error = '数据生成成功'
        return JsonResponse(ret.dict)


class EditBz(APIView):
    def get(self, request):
        """
        修改班子统计信息表中的是否测评
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            cePing = request.GET.get('cePing')  # 接收前台传过来的是否测评
            number = request.GET.get('number')  # 接收前台传过来单位代码
            BzTjInfo.objects.filter(number_id=number).update(cePing=cePing)
        except Exception as e:
            ret.code = 0
            ret.error = '修改失败'
            return JsonResponse(ret.dict)
        ret.code = 1
        ret.error = '修改成功'
        return JsonResponse(ret.dict)

# 显示所有部门信息
class GetDepartment(View):
    def get(self,request):
        try:
            obj_department=Department.objects.all().values()
            departments=list(obj_department)
            return JsonResponse({'code': 1, 'data': departments})
        except Exception as e:
            return JsonResponse({'code':0,'msg':"获取部门信息出现异常，具体错误：" + str(e)})

class AddDepartment(View):
    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        try:
            obj_department=Department(
                department=data['department'],
                number=data['number'],
                category=data['category']
            )
            obj_department.save()
            department=Department.objects.all().values()
            department=list(department)
            # 添加成功，返回所有数据
            return JsonResponse({'code': 1, 'data': department})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "添加部门信息出现异常，具体原因：" + str(e)})

class EditDepartment(View):
    def post(self,request):
        # 接受前端传递过来的数值
        data=json.loads(request.body.decode('utf-8'))
        try:
            obj_department=Department.objects.get(id=data['id'])
            obj_department.department=data['department']
            obj_department.number=data['number']
            obj_department.category=data['category']
            obj_department.save()
            department=Department.objects.all().values()
            department=list(department)
            return JsonResponse({'code':1,'data': department})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "修改保存到数据库出现异常，具体原因：" + str(e)})

class DeleteDepartment(View):
    def post(self,request):
        data=json.loads(request.body.decode('utf-8'))
        try:
            obj_department=Department.objects.get(id=data['id'])
            obj_department.delete()
            department=Department.objects.all().values()
            department=list(department)
            return JsonResponse({'code': 1, 'data': department})
        except Exception as e:
            return JsonResponse({'code': 0, 'msg': "删除部门信息出现异常，具体原因：" + str(e)})





