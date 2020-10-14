import pandas

from utils.random_name import get_random_str
from rest_framework.views import APIView
from utils.base_response import BaseResponse
from utils.desktop_path import get_desktop_path
from django.http import JsonResponse
from rest_framework.response import Response
from utils.excel import importdata, importdata2, exportdata
from houtai import settings
import os
import datetime
import time
from Renyuan.models import Ceping, Beiceping
from Bumen.models import Department
from Fangan.models import BzTjInfo, jggbIndexWeight, xygbIndexWeight, zsdwgbIndexWeight
from Result.models import Gbresult, Bzresult


# Create your views here.
def import_ceping(request):
    """
    导入测评人员
    :param request:
    :return:
    """
    foreignkey = ['department', 'rank_id', 'post_id']  # 记录外键
    # 接收excel文件存储到Media文件夹
    rev_file = request.FILES.get('excel')
    # 判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': 'Excel文件不存在'})
    # 获得一个唯一的名字：uuid+hash
    new_name = get_random_str()
    # 准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1])
    # 开始写入磁盘
    try:
        f = open(file_path, 'wb')
        # 分多次写入
        for i in rev_file.chunks():
            f.write(i)
        f.close()
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '写入失败，请联系管理员'})
    # 读取存储在Media文件夹的数据
    ex_data = importdata(file_path, Ceping, foreignkey)
    return JsonResponse({'code': 1, 'msg': ex_data})


def import_beiceping(request):
    """
    导入被测评人员
    :param request:
    :return:
    """
    foreignkey = ['department', 'rank_id', 'department_num']  # 记录外键
    # 接收excel文件存储到Media文件夹
    rev_file = request.FILES.get('excel')
    # 判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': 'Excel文件不存在'})
    # 获得一个唯一的名字：uuid+hash
    new_name = get_random_str()
    # 准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1])
    # 开始写入磁盘
    try:
        f = open(file_path, 'wb')
        # 分多次写入
        for i in rev_file.chunks():
            f.write(i)
        f.close()
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '写入失败，请联系管理员'})
    # 读取存储在Media文件夹的数据
    ex_data = importdata2(file_path, Beiceping, foreignkey)
    return JsonResponse({'code': 1, 'msg': ex_data})


def import_department(request):
    """
    导入单位表
    :param request:
    :return:
    """
    foreignkey = []  # 记录外键
    # 接收excel文件存储到Media文件夹
    rev_file = request.FILES.get('excel')
    # 判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': 'Excel文件不存在'})
    # 获得一个唯一的名字：uuid+hash
    new_name = get_random_str()
    # 准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1])
    # 开始写入磁盘
    try:
        f = open(file_path, 'wb')
        # 分多次写入
        for i in rev_file.chunks():
            f.write(i)
        f.close()
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '写入失败，请联系管理员'})
    # 读取存储在Media文件夹的数据
    ex_data = importdata(file_path, Department, foreignkey)
    return JsonResponse({'code': 1, 'msg': ex_data})


def import_lingdaobanzi(request):
    """
    导入领导班子统计信息表
    :param request:
    :return:
    """
    foreignkey = ['department', 'number']  # 记录外键
    # 接收excel文件存储到Media文件夹
    rev_file = request.FILES.get('excel')
    # 判断是否有文件
    if not rev_file:
        return JsonResponse({'code': 0, 'msg': 'Excel文件不存在'})
    # 获得一个唯一的名字：uuid+hash
    new_name = get_random_str()
    # 准备写入的URL
    file_path = os.path.join(settings.MEDIA_ROOT, new_name + os.path.splitext(rev_file.name)[1])
    # 开始写入磁盘
    try:
        f = open(file_path, 'wb')
        # 分多次写入
        for i in rev_file.chunks():
            f.write(i)
        f.close()
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': '写入失败，请联系管理员'})
    # 读取存储在Media文件夹的数据
    ex_data = importdata(file_path, BzTjInfo, foreignkey)
    return JsonResponse({'code': 1, 'msg': ex_data})

# def export_bzresult(request):
#     """
#     导出班子考核汇总表
#     默认导出到桌面
#     :param request:
#     :return:
#     """
#     ret = BaseResponse()
#     try:
#         path = get_desktop_path()+'\班子考核汇总表.xlsx'
#         exportdata(path, Bzresult)
#         ret.code = 210
#         ret.data = '数据导出成功'
#     except Exception as e:
#         ret.code = 211
#         ret.error = '数据导出失败'
#         return JsonResponse(ret.dict)
#     return JsonResponse(ret.dict)


class Export_excel(APIView):
    def post(self, request):
        """
        导出数据
        表头还是数据库的英文表头，没有变成中文
        :param request:
        :return:
        前台需要传给后台三个参数：
        1.文件名
        2.如果是导出数据库的就传数据表名
        3.如果是自定义数据，就将数据传过来
        """
        ret = BaseResponse()
        recept = request.data
        try:
            data = recept['data']  # 自定义数据
            filename = recept['filename']  # 文件名
            table = recept['table']  # 数据表名
            path = get_desktop_path() + r'\{}'.format(filename)
            if table != '':
                table = globals()[table]  # 可以将字符串转换成类名
            if table == '':
                exportdata(path, 0, data)
            if data == '':
                exportdata(path, table, 0)
        except Exception as e:
            ret.code = 211
            ret.error = '数据导出失败'
            return Response(ret.dict)
        ret.code = 210
        ret.data = '数据导出成功'
        return Response(ret.dict)


class Export_report_excel(APIView):
    def post(self, request):
        """
        导出报表excel
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            # 接收数据
            data = request.data
            year = data['year']
            flag = data['flag']
            category = data['category']
            # 判断条件是否为空
            if not year:
                ret.code = 1
                ret.data = '请选择年份'
                return Response(ret.dict)
            if not category:
                ret.code = 2
                ret.data = '请选择单位类别'
                return Response(ret.dict)
            # 处理文件名
            if flag:
                filename = '{}年度{}中层干部考核结果排名（{}）.xlsx'.format(year, category, flag)
            else:
                filename = '{}年度{}全体中层干部考核结果排名.xlsx'.format(year, category, flag)
            # 处理导出路径
            path = get_desktop_path() + r'\{}'.format(filename)
            # 处理表头和数据
            if category == '机关':
                jg_index = list(jggbIndexWeight.objects.filter(code__isnull=False, weight__isnull=False).values_list('index'))
                if flag:
                    columnname = ['单位', '姓名', '最终分数', '全校综合排名', '机关分类排名']
                    value = ['department', 'name', 'score', 'rankingOfAll']
                else:
                    columnname = ['单位', '姓名', '最终分数', '全校综合排名', '机关综合排名']
                    value = ['department', 'name', 'score', 'rankingOfAll', 'rankingofCategory']
                # 最终表头
                for i in range(0, len(jg_index)):
                    columnname.insert(i + 2, jg_index[i][0])
                # 查找的参数
                for i in range(0, len(jg_index)):
                    value.insert(i + 2, 'index{}'.format(i + 1))
            elif category == '学院':
                xy_index = list(xygbIndexWeight.objects.filter(code__isnull=False, weight__isnull=False).values_list('index'))
                if flag:
                    columnname = ['单位', '姓名', '最终分数', '学院综合排名', '学院分类排名']
                    value = ['department', 'name', 'score', 'rankingofCategory']
                else:
                    columnname = ['单位', '姓名', '最终分数', '全校综合排名', '学院综合排名']
                    value = ['department', 'name', 'score', 'rankingOfAll', 'rankingofCategory']
                for i in range(0, len(xy_index)):
                    columnname.insert(i + 2, xy_index[i][0])
                for i in range(0, len(xy_index)):
                    value.insert(i + 2, 'index{}'.format(i + 1))
            elif category == '直属单位':
                zsdw_index = list(zsdwgbIndexWeight.objects.filter(code__isnull=False, weight__isnull=False).values_list('index'))
                if flag:
                    columnname = ['单位', '姓名', '最终分数', '直属单位综合排名', '直属单位分类排名']
                    value = ['department', 'name', 'score', 'rankingofCategory']
                else:
                    columnname = ['单位', '姓名', '最终分数', '全校综合排名', '直属单位综合排名']
                    value = ['department', 'name', 'score', 'rankingOfAll', 'rankingofCategory']
                for i in range(0, len(zsdw_index)):
                    columnname.insert(i + 2, zsdw_index[i][0])
                for i in range(0, len(zsdw_index)):
                    value.insert(i + 2, 'index{}'.format(i + 1))
            if flag:
                data = Gbresult.objects.filter(category=category, beiKaoHe__contains=flag). \
                    values(*value).order_by('rankingOfAll')
                for i in range(0, len(data)):
                    data[i]['rank'] = i+1
            else:
                data = Gbresult.objects.filter(category=category). \
                    values(*value).order_by('rankingofCategory')
            data = pandas.DataFrame(data)
            data.to_excel(path, na_rep='', header=columnname, index=False)
        except Exception as e:
            ret.code = 0
            ret.error = '导出失败'
            return Response(ret.dict)
        ret.code = 3
        ret.data = '导出成功'
        return Response(ret.dict)


class Export_linereport(APIView):
    def get(self, request):
        """
        导出带有折线图报表excel
        :param request:
        :return:
        """
        ret = BaseResponse()
        try:
            year = datetime.datetime.now().year  # 当前年份
            department = Gbresult.objects.filter(category='学院').values('department').distinct()  # 学院单位
            random_file = get_random_str()  # 创建随机文件名
            os.mkdir(get_desktop_path() + '\\{}年度反馈给各学院的结果报表{}'.format(year, random_file))  # 先创建一个文件夹
            xy_index = list(xygbIndexWeight.objects.filter(code__isnull=False, weight__isnull=False).values_list('index'))
            score_index = []
            for each in xy_index:
                score_index.append(each[0])
            columnname = ['单位', '姓名', '最终分数']
            value = ['department', 'name', 'score']
            for i in range(0, len(xy_index)):
                columnname.insert(i + 2, xy_index[i][0])
            for i in range(0, len(xy_index)):
                value.insert(i + 2, 'index{}'.format(i + 1))
            # 需要转换成数值型的列
            value1 = []
            for each_value in value:
                if 'index' in each_value:
                    value1.append(each_value)
            value1.append('score')

            for each_department in department:
                max_score = 0  # 最小值
                min_score = 100  # 最大值
                data = Gbresult.objects.filter(department=each_department['department']). \
                    values(*value).order_by('rankingOfDep')
                # 转换为数值型
                for each_data in data:
                    for each in value1:
                        each_data[each] = float(each_data[each])
                        if each_data[each] > max_score:
                            max_score = each_data[each]
                        if each_data[each] < min_score:
                            min_score = each_data[each]

                filename = '{}年{}单位中层干部民主测评结果.xlsx'.format(year, each_department['department'])
                # 处理导出路径
                # path = get_desktop_path() + r'\反馈给各学院的结果报表{}\{}'.format(random_file, filename)
                path = get_desktop_path() + '\\{}年度反馈给各学院的结果报表{}\\{}'.format(year, random_file, filename)
                data = pandas.DataFrame(data)
                # data.to_excel(path, na_rep='', header=columnname, index=False)
                sheet_name = 'Sheet1'
                writer = pandas.ExcelWriter(path, engine='xlsxwriter')
                # data = list(data)[0]
                data.to_excel(writer, sheet_name=sheet_name, na_rep='', header=columnname, index=False)

                # 导出折线图
                max_row = len(data)
                workbook = writer.book
                worksheet = writer.sheets[sheet_name]
                chart = workbook.add_chart({'type': 'line'})
                # Configure the series of the chart from the dataframe data.
                for i in range(0, max_row):
                    row = i + 1
                    chart.add_series({
                        'name': ['Sheet1', row, 1],
                        'categories': ['Sheet1', 0, 2, 0, 14],
                        'values': ['Sheet1', row, 2, row, 14],
                        # 'name': ['Sheet1', 0, col],
                        # 'categories': ['Sheet1', 1, 0, max_row, 0],
                        # 'values': ['Sheet1', 1, col, max_row, col],
                    })
                # Configure the chart axes.
                chart.set_x_axis({'name': '{}年{}单位中层干部民主测评结果'.format(year, each_department['department'])})
                chart.set_y_axis({'name': '得分', 'major_gridlines': {'visible': False}, 'min': min_score, 'max': max_score})
                # Insert the chart into the worksheet.
                worksheet.insert_chart('G2', chart)
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
        except Exception as e:
            ret.code = 0
            ret.error = '导出失败'
            return Response(ret.dict)
        ret.code = 1
        ret.data = '导出成功'
        return Response(ret.dict)