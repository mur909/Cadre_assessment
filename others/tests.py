import datetime
import shutil

import pandas
from django.test import TestCase
import winreg
# Create your tests here.

import pandas as pd
import random
from houtai import settings
from houtai.settings import BASE_DIR
from utils.desktop_path import get_desktop_path
from utils.random_name import get_random_str
import zipfile
import os
import zipstream

import zipfile  # 引入zip管理模块
import os
import sys  # 引入sys模块，获取脚本所在目录


def compressFolder(folderPath, compressPathName):
    '''
    :param folderPath: 文件夹路径
    :param compressPathName: 压缩包路径
    :return:
    '''
    zip = zipfile.ZipFile(compressPathName, 'w', zipfile.ZIP_DEFLATED)

    for path, dirNames, fileNames in os.walk(folderPath):
        fpath = path.replace(folderPath, '')
        for name in fileNames:
            fullName = os.path.join(path, name)

            name = fpath + '\\' + name
            zip.write(fullName, name)

    zip.close()





def panda_chart(df_list, cols, title_x, title_y):
    """
    data of narray
    index of data_frame:  [0,1,2,3]
    cols numbers of static columns
    """
    writer = pd.ExcelWriter('pandas_chart_columns2.xlsx', engine='xlsxwriter')
    for i, df in enumerate(df_list):
        # df = pd.DataFrame(data, index=None, columns=["姓名", "饱和度", "人力"])
        sheet_name = f'Sheet{i}'
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        chart = workbook.add_chart({'type': 'column'})
        # set colors for the chart each type .
        colors = ['#E41A1C', '#377EB8']  # , '#4DAF4A', '#984EA3', '#FF7F00']
        # Configure the series of the chart from the dataframe data.
        for col_num in range(1, cols + 1):
            chart.add_series({
                'name': [f'{sheet_name}', 0, col_num],
                'categories': [f'{sheet_name}', 1, 0, 4, 0],  # axis_x start row ,start col,end row ,end col
                'values': [f'{sheet_name}', 1, col_num, 4, col_num],  # axis_y value of
                'fill': {'color': colors[col_num - 1]},  # each type color choose
                'overlap': -10,
            })
        # Configure the chart axes.
        chart.set_x_axis({'name': f'{title_x}'})
        chart.set_y_axis({'name': f'{title_y}', 'major_gridlines': {'visible': False}})
        chart.set_size({'width': 900, 'height': 400})
        # Insert the chart into the worksheet.
        worksheet.insert_chart('H2', chart)
    writer.save()


def panda_line_chart():
    # Create some sample data to plot.
    # data = {
    #     "department": ["能源研究院", "能源研究院"],
    #     "name": ["李华明", "何志霞"],
    #     "index1": [49.1282, 42.3448],
    #     "index2": [48.9231, 42.069],
    #     "index3": [48.1538, 41.2414],
    #     "index4": [48.1026, 41.2414],
    #     "index5": [41.1282, 40.4138],
    #     "index6": [48.5128, 41.5172],
    #     "index7": [48.6154, 41.5172],
    #     "index8": [48.1026, 41.2414],
    #     "index9": [48.2051, 41.1034],
    #     "index10": [48.4103, 41.3793],
    #     "index11": [40.9231, 40],
    #     "index12": [48.7692, 41.6552],
    #     "score": [47.245179487179, 41.30924137931]
    # }
    max_row = 21
    categories = ['Node 1', 'Node 2', 'Node 3', 'Node 4']
    index_1 = range(0, max_row, 1)
    multi_iter1 = {'index': index_1}
    print('1--{}'.format(multi_iter1))
    for category in categories:
        multi_iter1[category] = [random.randint(10, 100) for x in index_1]
        print('2--{}'.format(multi_iter1[category]))
    print('3--{}'.format(multi_iter1))
    # Create a Pandas dataframe from the data.
    index_2 = multi_iter1.pop('index')
    print('4--{}'.format(index_2))
    df = pd.DataFrame(multi_iter1, index=index_2)
    print('5--{}'.format(len(df)))
    df = df.reindex(columns=sorted(df.columns))
    print('6--{}'.format(df))
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    sheet_name = 'Sheet1'
    writer = pd.ExcelWriter('pandas_chart_line.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name)
    # Access the XlsxWriter workbook and worksheet objects from the dataframe.
    workbook = writer.book
    print(workbook)
    worksheet = writer.sheets[sheet_name]
    print(worksheet)
    # Create a chart object.
    chart = workbook.add_chart({'type': 'line'})
    # Configure the series of the chart from the dataframe data.
    for i in range(len(categories)):
        col = i + 1
        chart.add_series({
            'name': ['Sheet1', 0, col],
            'categories': ['Sheet1', 1, 0, max_row, 0],
            'values': ['Sheet1', 1, col, max_row, col],
        })
    # Configure the chart axes.
    chart.set_x_axis({'name': 'Index'})
    chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})
    # Insert the chart into the worksheet.
    worksheet.insert_chart('G2', chart)
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def demo():
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
        path = get_desktop_path() + '\\{}年度反馈给各学院的结果报表{}'.format(year, random_file)
        print(path)
        print(os.path.isdir(path))
        return
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


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Renyuan.models import Ceping
    from others.models import User, Role
    from Fangan.models import jggbIndexWeight, xygbIndexWeight
    from Result.models import Gbresult

    filepath = settings.REPORT_ROOT
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)
