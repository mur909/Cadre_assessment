import pandas
from django.http import HttpResponse


# 批量导入数据(速度快)
def importdata(localpath: str, db: str, foreignkey):
    data = pandas.read_excel(localpath, dtype='str', keep_default_na=False)  # 读取本地上传的excel表内容, dtype='str'防止读取001为1这种情况。
    verbosename = db._meta.fields  # 获取被导入数据库的字段
    rows = data.shape[0]  # 获取excel表的行数
    columns = data.shape[1]  # 获取excel表的列数
    querysetlist = []  # 用于储存数据
    eachdata = {}  # 用于储存每一行数据
    # 外键需要添加_id，与数据库中的字段保持一致
    for i in range(len(verbosename)):
        if verbosename[i].name in foreignkey:  # 判断是否为外键
            verbosename[i].name = verbosename[i].name + '_id'
    if len(verbosename) == columns:  # 必须保证二者长度一致，顺序一致。
        for i in range(rows):
            for j in range(len(verbosename)):
                eachdata[verbosename[j].name] = data.iloc[i, j]  # 不会包括表头
            querysetlist.append(db(**eachdata))
        try:
            db.objects.bulk_create(querysetlist)  # 批量导入数据
            msg = '数据导入成功,导入数据共计{}条'.format(rows)
        except Exception as e:
            print('报错信息：{}'.format(e))
            msg = '数据导入失败'
        return msg
    else:
        msg = '数据导入失败！请检查excel表。'
        return msg


# 逐个导入数据(速度慢)
def importdata2(localpath: str, db: str, foreignkey):
    data = pandas.read_excel(localpath, dtype='str', keep_default_na=False)  # 读取本地上传的excel表内容, dtype='str'防止读取001为1这种情况。
    verbosename = db._meta.fields  # 获取被导入数据库的字段
    # for i in range(0, len(verbosename)):
    #     print(verbosename[i].name)
    rows = data.shape[0]  # 获取excel表的行数
    columns = data.shape[1]  # 获取excel表的列数
    eachdata = {}  # 用于储存每一行数据
    # 外键需要添加_id，与数据库中的字段保持一致
    for i in range(len(verbosename)):
        if verbosename[i].name in foreignkey:  # 判断是否为外键
            verbosename[i].name = verbosename[i].name + '_id'
    if len(verbosename) == columns:  # 必须保证二者长度一致，顺序一致。
        for i in range(rows):
            for j in range(len(verbosename)):
                eachdata[verbosename[j].name] = data.iloc[i, j]  # 不会包括表头
            try:
                db.objects.create(**eachdata)
                msg = '数据导入成功，共计{}条'.format(rows)
            except Exception as e:
                print('报错信息：{}'.format(e))
                msg = '数据导入失败'
            # return msg
    else:
        msg = '数据导入失败！请检查excel表。'
    return msg


#  导出数据库数据或者指定数据
def exportdata(localpath, db, data):
    # 导出数据库数据
    if db != 0:
        verbosename = db._meta.fields
        columnname = []  # 存储字段名
        for i in range(len(verbosename)):
            columnname.append(verbosename[i].name)
        info = db.objects.values_list()  # 查询数据库数据
    # 导出指定数据
    # 这里data传过来的有多个表头，所以取第一个表头
    elif data != 0:
        columnname = []
        for eachData in data[0]:
            columnname.append(eachData)
        info = data
    data = pandas.DataFrame(info)
    data.to_excel(localpath, na_rep='', header=columnname, index=False)