from django.test import TestCase
import os
# Create your tests here.


def calculation():
    Xi = []
    molecular = 0
    scoreLst = [
        {'score': 70, 'topScore': 84, 'credits': 3.0},
        {'score': 86, 'topScore': 91, 'credits': 1.0},
        {'score': 81, 'topScore': 88, 'credits': 1.0},
        {'score': 88, 'topScore': 95, 'credits': 2.0},
        {'score': 78, 'topScore': 99, 'credits': 2.0},
        {'score': 81, 'topScore': 99, 'credits': 2.0},
        {'score': 85, 'topScore': 91, 'credits': 3.0},
        {'score': 80, 'topScore': 90, 'credits': 2.0},
        {'score': 79, 'topScore': 82, 'credits': 2.0},
        {'score': 85, 'topScore': 93, 'credits': 2.0},
        {'score': 70, 'topScore': 90, 'credits': 1.0}
    ]
    for i in range(0, len(scoreLst)):
        Xi.append(90*scoreLst[i]['score']/scoreLst[i]['topScore'])
    for i in range(0, len(scoreLst)):
        molecular = molecular + Xi[i]*scoreLst[i]['credits']
    G2 = molecular/21
    print(G2)



def test():
    gb_obj = Gbresult.objects.values('IDcard', 'score')
    total = len(gb_obj)  # 总人数
    print(total)
    top_ten = int(total * 0.1)  # 前百分之十的排名
    print(top_ten)
    top_ten_score = Gbresult.objects.filter(rankingOfAll=top_ten).values('score')  # 前百分之十最后一名的分数
    print(top_ten_score[0]['score'])


def test1():
    gb_obj = Gbresult.objects.values('IDcard', 'score').order_by('score').reverse()
    total = len(gb_obj)  # 总人数
    print(total)
    last_ten = total - int(total*0.1) + 1
    print(last_ten)


class A(object):
    def __init__(self):
        names = self.__dict__
        index_obj = jggbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
        for i in range(0, len(index_obj)):
            names['index'+str(i+1)+'_weight'] = index_obj[i]['weight']


def test2():
    # a = A().__dict__
    index_weight = []
    index_obj = jggbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])
    print(index_weight)
    print(index_weight[0])
    print(len(index_weight))


def test3():
    # 机关干部指标权重
    index_weight = []
    index_obj = jggbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])

    # 干部测评权重表
    index19_weight = GbCpWeight.objects.filter(code='005').values_list('weight', flat=True)[0]  # 机关校领导权重
    index20_weight = GbCpWeight.objects.filter(code='006').values_list('weight', flat=True)[0]  # 党政处级权重
    index21_weight = GbCpWeight.objects.filter(code='007').values_list('weight', flat=True)[0]  # 党政科级及职工权重
    index22_weight = GbCpWeight.objects.filter(code='008').values_list('weight', flat=True)[0]  # 学院领导权重
    index23_weight = GbCpWeight.objects.filter(code='009').values_list('weight', flat=True)[0]  # 学院相关权重

    beiceping_id = jggbTongji.objects.values_list('beiceping_id').distinct()  # 获取所有被测评人的id,并去重

    # 处理每一个被测评人的分数
    for i in range(0, len(beiceping_id)):
        count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = 0
        sum0 = sum01 = sum02 = sum03 = sum04 = sum05 = sum06 = sum07 = sum08 = sum09 = sum010 = sum011 = sum012 = sum013 = sum014 = sum015 = sum016 = sum017 = sum018 = 0
        sum1 = sum11 = sum12 = sum13 = sum14 = sum15 = sum16 = sum17 = sum18 = sum19 = sum110 = sum111 = sum112 = sum113 = sum114 = sum115 = sum116 = sum117 = sum118 = 0
        sum2 = sum21 = sum22 = sum23 = sum24 = sum25 = sum26 = sum27 = sum28 = sum29 = sum210 = sum211 = sum212 = sum213 = sum214 = sum215 = sum216 = sum217 = sum218 = 0
        sum3 = sum31 = sum32 = sum33 = sum34 = sum35 = sum36 = sum37 = sum38 = sum39 = sum310 = sum311 = sum312 = sum313 = sum314 = sum315 = sum316 = sum317 = sum318 = 0
        sum4 = sum41 = sum42 = sum43 = sum44 = sum45 = sum46 = sum47 = sum48 = sum49 = sum410 = sum411 = sum412 = sum413 = sum414 = sum415 = sum416 = sum417 = sum418 = 0
        sum5 = sum51 = sum52 = sum53 = sum54 = sum55 = sum56 = sum57 = sum58 = sum59 = sum510 = sum511 = sum512 = sum513 = sum514 = sum515 = sum516 = sum517 = sum518 = 0
        sum6 = sum61 = sum62 = sum63 = sum64 = sum65 = sum66 = sum67 = sum68 = sum69 = sum610 = sum611 = sum612 = sum613 = sum614 = sum615 = sum616 = sum617 = sum618 = 0
        sum7 = sum71 = sum72 = sum73 = sum74 = sum75 = sum76 = sum77 = sum78 = sum79 = sum710 = sum711 = sum712 = sum713 = sum714 = sum715 = sum716 = sum717 = sum718 = 0
        each_beiceping_id = beiceping_id[i][0]  # 得到每一个被测评人的id
        dep_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('department_num', flat=True)[
            0]  # 被测评者的单位代码
        rank_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('rank_id_id', flat=True)[
            0]  # 被测评者的职级代码
        each_obj = jggbTongji.objects.filter(beiceping=each_beiceping_id, giveup=0)  # 得到这个被测评人在统计表中的所有数据， 不包括放弃测评的
        count = len(each_obj)  # 得到该被测评人的测评总数

        # 对每一个被测评者的每一条数据进行整理
        for j in range(0, count):
            cp_dep_num = each_obj[j].depNum_id  # 测评者的单位代码
            ceping_rank_id = each_obj[j].rankNum_id  # 测评者的职级代码
            # 机关校领导
            if ceping_rank_id == '001':
                count0 += 1
                sum01 = (sum01 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum02 = (sum02 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum03 = (sum03 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum04 = (sum04 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum05 = (sum05 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum06 = (sum06 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum07 = (sum07 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum08 = (sum08 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum09 = (sum09 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum010 = (sum010 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum011 = (sum011 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum012 = (sum012 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum013 = (sum013 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum014 = (sum014 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum015 = (sum015 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum016 = (sum016 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum017 = (sum017 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum018 = (sum018 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 党政处级
            if ceping_rank_id == '002' and cp_dep_num > '100':
                count1 += 1
                sum11 = (sum11 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum12 = (sum12 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum13 = (sum13 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum14 = (sum14 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum15 = (sum15 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum16 = (sum16 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum17 = (sum17 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum18 = (sum18 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum19 = (sum19 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum110 = (sum110 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum111 = (sum111 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum112 = (sum112 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum113 = (sum113 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum114 = (sum114 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum115 = (sum115 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum116 = (sum116 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum117 = (sum117 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum118 = (sum118 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 党政科级及职工
            if ceping_rank_id > '002' and cp_dep_num > '100':
                count2 += 1
                sum21 = (sum21 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum22 = (sum22 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum23 = (sum23 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum24 = (sum24 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum25 = (sum25 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum26 = (sum26 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum27 = (sum27 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum28 = (sum28 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum29 = (sum29 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum210 = (sum210 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum211 = (sum211 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum212 = (sum212 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum213 = (sum213 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum214 = (sum214 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum215 = (sum215 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum216 = (sum216 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum217 = (sum217 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum218 = (sum218 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 学院领导
            if ceping_rank_id == '002' and cp_dep_num > '300':
                count3 += 1
                sum31 = (sum31 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum32 = (sum32 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum33 = (sum33 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum34 = (sum34 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum35 = (sum35 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum36 = (sum36 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum37 = (sum37 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum38 = (sum38 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum39 = (sum39 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum310 = (sum310 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum311 = (sum311 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum312 = (sum312 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum313 = (sum313 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum314 = (sum314 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum315 = (sum315 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum316 = (sum316 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum317 = (sum317 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum318 = (sum318 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 学院相关
            if ceping_rank_id > '002' and cp_dep_num > '300':
                count4 += 1
                sum41 = (sum41 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum42 = (sum42 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum43 = (sum43 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum44 = (sum44 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum45 = (sum45 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum46 = (sum46 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum47 = (sum47 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum48 = (sum48 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum49 = (sum49 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum410 = (sum410 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum411 = (sum411 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum412 = (sum412 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum413 = (sum413 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum414 = (sum414 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum415 = (sum415 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum416 = (sum416 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum417 = (sum417 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum418 = (sum418 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 上级
            if ceping_rank_id < rank_num:
                count5 += 1
                sum51 = (sum51 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum52 = (sum52 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum53 = (sum53 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum54 = (sum54 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum55 = (sum55 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum56 = (sum56 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum57 = (sum57 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum58 = (sum58 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum59 = (sum59 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum510 = (sum510 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum511 = (sum511 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum512 = (sum512 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum513 = (sum513 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum514 = (sum514 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum515 = (sum515 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum516 = (sum516 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum517 = (sum517 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum518 = (sum518 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 同级
            if ceping_rank_id == rank_num:
                count6 += 1
                sum61 = (sum61 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum62 = (sum62 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum63 = (sum63 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum64 = (sum64 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum65 = (sum65 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum66 = (sum66 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum67 = (sum67 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum68 = (sum68 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum69 = (sum69 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum610 = (sum610 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum611 = (sum611 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum612 = (sum612 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum613 = (sum613 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum614 = (sum614 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum615 = (sum615 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum616 = (sum616 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum617 = (sum617 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum618 = (sum618 + each_obj[j].index18 if each_obj[j].index18 else 0)
            # 下级
            if ceping_rank_id > rank_num:
                count7 += 1
                sum71 = (sum71 + each_obj[j].index1 if each_obj[j].index1 else 0)
                sum72 = (sum72 + each_obj[j].index2 if each_obj[j].index2 else 0)
                sum73 = (sum73 + each_obj[j].index3 if each_obj[j].index3 else 0)
                sum74 = (sum74 + each_obj[j].index4 if each_obj[j].index4 else 0)
                sum75 = (sum75 + each_obj[j].index5 if each_obj[j].index5 else 0)
                sum76 = (sum76 + each_obj[j].index6 if each_obj[j].index6 else 0)
                sum77 = (sum77 + each_obj[j].index7 if each_obj[j].index7 else 0)
                sum78 = (sum78 + each_obj[j].index8 if each_obj[j].index8 else 0)
                sum79 = (sum79 + each_obj[j].index9 if each_obj[j].index9 else 0)
                sum710 = (sum710 + each_obj[j].index10 if each_obj[j].index10 else 0)
                sum711 = (sum711 + each_obj[j].index11 if each_obj[j].index11 else 0)
                sum712 = (sum712 + each_obj[j].index12 if each_obj[j].index12 else 0)
                sum713 = (sum713 + each_obj[j].index13 if each_obj[j].index13 else 0)
                sum714 = (sum714 + each_obj[j].index14 if each_obj[j].index14 else 0)
                sum715 = (sum715 + each_obj[j].index15 if each_obj[j].index15 else 0)
                sum716 = (sum716 + each_obj[j].index16 if each_obj[j].index16 else 0)
                sum717 = (sum717 + each_obj[j].index17 if each_obj[j].index17 else 0)
                sum718 = (sum718 + each_obj[j].index18 if each_obj[j].index18 else 0)
        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09, sum010, sum011, sum012, sum013,
                    sum014,
                    sum015, sum016, sum017, sum018]
        sum1_lst = [sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19, sum110, sum111, sum112, sum113,
                    sum114,
                    sum115, sum116, sum117, sum118]
        sum2_lst = [sum21, sum22, sum23, sum24, sum25, sum26, sum27, sum28, sum29, sum210, sum211, sum212, sum213,
                    sum214,
                    sum215, sum216, sum217, sum218]
        sum3_lst = [sum31, sum32, sum33, sum34, sum35, sum36, sum37, sum38, sum39, sum310, sum311, sum312, sum313,
                    sum314,
                    sum315, sum316, sum317, sum318]
        sum4_lst = [sum41, sum42, sum43, sum44, sum45, sum46, sum47, sum48, sum49, sum410, sum411, sum412, sum413,
                    sum414,
                    sum415, sum416, sum417, sum418]
        sum5_lst = [sum51, sum52, sum53, sum54, sum55, sum56, sum57, sum58, sum59, sum510, sum511, sum512, sum513,
                    sum514,
                    sum515, sum516, sum517, sum518]
        sum6_lst = [sum61, sum62, sum63, sum64, sum65, sum66, sum67, sum68, sum69, sum610, sum611, sum612, sum613,
                    sum614,
                    sum615, sum616, sum617, sum618]
        sum7_lst = [sum71, sum72, sum73, sum74, sum75, sum76, sum77, sum78, sum79, sum710, sum711, sum712, sum713,
                    sum714,
                    sum715, sum716, sum717, sum718]
        print(sum0_lst)
        print(count0, count1, count2, count3, count4, count5, count6, count7)
        print('------------------------------')
            

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "houtai.settings")
    import django

    django.setup()
    from Result.models import Gbresult
    from Fangan.models import jggbIndexWeight, GbCpWeight, jggbTongji
    from Renyuan.models import Beiceping, Ceping
    try:
        calculation()
    except Exception as e:
        print(e)