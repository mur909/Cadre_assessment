from Fangan.models import xygbTongji, jggbTongji, zsdwgbTongji, xybzTongji, zsdwbzTongji, \
    xygbResult, jggbResult, zsdwgbResult, xybzResult, zsdwbzResult, \
    xygbIndexWeight, jggbIndexWeight, zsdwgbIndexWeight, xybzIndexWeight, zsdwbzIndexWeight, GbCpWeight, BzCpWeight
from Renyuan.models import Beiceping


def xygbresult():
    """
    计算学院干部结果表
    :return:
    """
    # 学院干部指标权重
    index_weight = []
    index_obj = xygbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])

    # 干部测评权重表
    index19_weight = GbCpWeight.objects.filter(code='001').values_list('weight', flat=True)[0]  # 学院校领导
    index20_weight = GbCpWeight.objects.filter(code='002').values_list('weight', flat=True)[0]  # 班子成员
    index21_weight = GbCpWeight.objects.filter(code='003').values_list('weight', flat=True)[0]  # 学院师生
    index22_weight = GbCpWeight.objects.filter(code='004').values_list('weight', flat=True)[0]  # 对口机关

    beiceping_id = xygbTongji.objects.values_list('beiceping_id').distinct()  # 获取所有被测评人的id,并去重

    # 处理每一个被测评人的分数
    for i in range(0, len(beiceping_id)):
        count0 = count1 = count2 = count3 = count4 = count5 = count6 = 0
        sum0 = sum01 = sum02 = sum03 = sum04 = sum05 = sum06 = sum07 = sum08 = sum09 = sum010 = sum011 = sum012 = sum013 = sum014 = sum015 = sum016 = sum017 = sum018 = 0
        sum1 = sum11 = sum12 = sum13 = sum14 = sum15 = sum16 = sum17 = sum18 = sum19 = sum110 = sum111 = sum112 = sum113 = sum114 = sum115 = sum116 = sum117 = sum118 = 0
        sum2 = sum21 = sum22 = sum23 = sum24 = sum25 = sum26 = sum27 = sum28 = sum29 = sum210 = sum211 = sum212 = sum213 = sum214 = sum215 = sum216 = sum217 = sum218 = 0
        sum3 = sum31 = sum32 = sum33 = sum34 = sum35 = sum36 = sum37 = sum38 = sum39 = sum310 = sum311 = sum312 = sum313 = sum314 = sum315 = sum316 = sum317 = sum318 = 0
        sum4 = sum41 = sum42 = sum43 = sum44 = sum45 = sum46 = sum47 = sum48 = sum49 = sum410 = sum411 = sum412 = sum413 = sum414 = sum415 = sum416 = sum417 = sum418 = 0
        sum5 = sum51 = sum52 = sum53 = sum54 = sum55 = sum56 = sum57 = sum58 = sum59 = sum510 = sum511 = sum512 = sum513 = sum514 = sum515 = sum516 = sum517 = sum518 = 0
        sum6 = sum61 = sum62 = sum63 = sum64 = sum65 = sum66 = sum67 = sum68 = sum69 = sum610 = sum611 = sum612 = sum613 = sum614 = sum615 = sum616 = sum617 = sum618 = 0

        each_beiceping_id = beiceping_id[i][0]  # 得到每一个被测评人的id
        # 被测评者的单位代码
        dep_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('department_num', flat=True)[0]
        # 被测评者的职级代码
        rank_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('rank_id_id', flat=True)[0]
        # 得到这个被测评人在统计表中的所有数据
        each_obj = xygbTongji.objects.filter(beiceping=each_beiceping_id, giveup=0)
        count = len(each_obj)  # 得到该被测评人的测评总数

        # 对每一个被测评者的每一条数据进行整理
        for j in range(0, count):
            cp_dep_num = each_obj[j].depNum_id  # 测评者的单位代码
            ceping_rank_id = each_obj[j].rankNum_id  # 测评者的职级代码
            # 判断测评者是否为校领导
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
            # 本单位中层干部
            if ceping_rank_id == '002' and dep_num == cp_dep_num:
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
            # 职工、学生代表（非中层干部）
            if ceping_rank_id > '002' and dep_num == cp_dep_num:
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
            # 其他参加考核的学院、机关、直属单位中层干部
            if ceping_rank_id != '001' and dep_num != cp_dep_num:
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
            # 上级
            if ceping_rank_id < rank_num:
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
            # 同级
            if ceping_rank_id == rank_num:
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
            # 下级
            if ceping_rank_id > rank_num:
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

        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09,
                    sum010, sum011, sum012, sum013, sum014, sum015, sum016, sum017, sum018]
        sum1_lst = [sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19,
                    sum110, sum111, sum112, sum113, sum114, sum115, sum116, sum117, sum118]
        sum2_lst = [sum21, sum22, sum23, sum24, sum25, sum26, sum27, sum28, sum29,
                    sum210, sum211, sum212, sum213, sum214, sum215, sum216, sum217, sum218]
        sum3_lst = [sum31, sum32, sum33, sum34, sum35, sum36, sum37, sum38, sum39,
                    sum310, sum311, sum312, sum313, sum314, sum315, sum316, sum317, sum318]
        sum4_lst = [sum41, sum42, sum43, sum44, sum45, sum46, sum47, sum48, sum49,
                    sum410, sum411, sum412, sum413, sum414, sum415, sum416, sum417, sum418]
        sum5_lst = [sum51, sum52, sum53, sum54, sum55, sum56, sum57, sum58, sum59,
                    sum510, sum511, sum512, sum513, sum514, sum515, sum516, sum517, sum518]
        sum6_lst = [sum61, sum62, sum63, sum64, sum65, sum66, sum67, sum68, sum69,
                    sum610, sum611, sum612, sum613, sum614, sum615, sum616, sum617, sum618]

        if count0 > 0:
            for i in range(0, len(index_weight)):
                sum0 = sum0 + sum0_lst[i] * index_weight[i]
            sum0 = sum0 / count0
            # sum0 = (um01 * zzpz_weight + sum02 * ddpx_weight + sum03 * gzsl_weight + sum04 * zznl_weight + sum05 * cxys_weight + sum06 * jltr_weight + sum07 * gzzf_weight + sum08 * gfgl_weight + sum09 * mbwc_weight + sum010 * bsxl_weight + sum011 * tcyj_weight + sum012 * ljzl_weight) / count0
        if count1 > 0:
            for i in range(0, len(index_weight)):
                sum1 = sum1 + sum1_lst[i] * index_weight[i]
            sum1 = sum1 / count1
            # sum1 = (sum11 * zzpz_weight + sum12 * ddpx_weight + sum13 * gzsl_weight + sum14 * zznl_weight + sum15 * cxys_weight + sum16 * jltr_weight + sum17 * gzzf_weight + sum18 * gfgl_weight + sum19 * mbwc_weight + sum110 * bsxl_weight + sum111 * tcyj_weight + sum112 * ljzl_weight) / count1
        if count2 > 0:
            for i in range(0, len(index_weight)):
                sum2 = sum2 + sum2_lst[i] * index_weight[i]
            sum2 = sum2 / count2
            # sum2 = (sum21 * zzpz_weight + sum22 * ddpx_weight + sum23 * gzsl_weight + sum24 * zznl_weight + sum25 * cxys_weight + sum26 * jltr_weight + sum27 * gzzf_weight + sum28 * gfgl_weight + sum29 * mbwc_weight + sum210 * bsxl_weight + sum211 * tcyj_weight + sum212 * ljzl_weight) / count2
        if count3 > 0:
            for i in range(0, len(index_weight)):
                sum3 = sum3 + sum3_lst[i] * index_weight[i]
            sum3 = sum3 / count3
            # sum3 = (sum31 * zzpz_weight + sum32 * ddpx_weight + sum33 * gzsl_weight + sum34 * zznl_weight + sum35 * cxys_weight + sum36 * jltr_weight + sum37 * gzzf_weight + sum38 * gfgl_weight + sum39 * mbwc_weight + sum310 * bsxl_weight + sum311 * tcyj_weight + sum312 * ljzl_weight) / count3
        if count4 > 0:
            for i in range(0, len(index_weight)):
                sum4 = sum4 + sum4_lst[i] * index_weight[i]
            sum4 = sum4 / count4
            # sum4 = (sum41 * zzpz_weight + sum42 * ddpx_weight + sum43 * gzsl_weight + sum44 * zznl_weight + sum45 * cxys_weight + sum46 * jltr_weight + sum47 * gzzf_weight + sum48 * gfgl_weight + sum49 * mbwc_weight + sum410 * bsxl_weight + sum411 * tcyj_weight + sum412 * ljzl_weight) / count4
        if count5 > 0:
            for i in range(0, len(index_weight)):
                sum5 = sum5 + sum5_lst[i] * index_weight[i]
            sum5 = sum5 / count5
            # sum5 = (sum51 * zzpz_weight + sum52 * ddpx_weight + sum53 * gzsl_weight + sum54 * zznl_weight + sum55 * cxys_weight + sum56 * jltr_weight + sum57 * gzzf_weight + sum58 * gfgl_weight + sum59 * mbwc_weight + sum510 * bsxl_weight + sum511 * tcyj_weight + sum512 * ljzl_weight) / count5
        if count6 > 0:
            for i in range(0, len(index_weight)):
                sum6 = sum6 + sum6_lst[i] * index_weight[i]
            sum6 = sum6 / count6
            # sum6 = (sum61 * zzpz_weight + sum62 * ddpx_weight + sum63 * gzsl_weight + sum64 * zznl_weight + sum65 * cxys_weight + sum66 * jltr_weight + sum67 * gzzf_weight + sum68 * gfgl_weight + sum69 * mbwc_weight + sum610 * bsxl_weight + sum611 * tcyj_weight + sum612 * ljzl_weight) / count6

        sum = sum0 * index19_weight + sum1 * index20_weight + sum2 * index21_weight + sum3 * index22_weight

        # 全体
        average1 = (sum01 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum11 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum21 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum31 * index22_weight / count3 if count3 > 0 else 0)

        average2 = (sum02 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum12 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum22 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum32 * index22_weight / count3 if count3 > 0 else 0)

        average3 = (sum03 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum13 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum23 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum33 * index22_weight / count3 if count3 > 0 else 0)

        average4 = (sum04 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum14 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum24 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum34 * index22_weight / count3 if count3 > 0 else 0)

        average5 = (sum05 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum15 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum25 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum35 * index22_weight / count3 if count3 > 0 else 0)

        average6 = (sum06 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum16 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum26 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum36 * index22_weight / count3 if count3 > 0 else 0)

        average7 = (sum07 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum17 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum27 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum37 * index22_weight / count3 if count3 > 0 else 0)

        average8 = (sum08 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum18 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum28 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum38 * index22_weight / count3 if count3 > 0 else 0)

        average9 = (sum09 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum19 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum29 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum39 * index22_weight / count3 if count3 > 0 else 0)

        average10 = (sum010 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum110 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum210 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum310 * index22_weight / count3 if count3 > 0 else 0)

        average11 = (sum011 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum111 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum211 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum311 * index22_weight / count3 if count3 > 0 else 0)

        average12 = (sum012 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum112 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum212 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum312 * index22_weight / count3 if count3 > 0 else 0)

        average13 = (sum013 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum113 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum213 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum313 * index22_weight / count3 if count3 > 0 else 0)

        average14 = (sum014 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum114 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum214 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum314 * index22_weight / count3 if count3 > 0 else 0)

        average15 = (sum015 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum115 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum215 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum315 * index22_weight / count3 if count3 > 0 else 0)

        average16 = (sum016 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum116 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum216 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum316 * index22_weight / count3 if count3 > 0 else 0)

        average17 = (sum017 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum117 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum217 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum317 * index22_weight / count3 if count3 > 0 else 0)

        average18 = (sum018 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum118 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum218 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum318 * index22_weight / count3 if count3 > 0 else 0)
        # 全体
        xygbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=average1,
            index2=average2,
            index3=average3,
            index4=average4,
            index5=average5,
            index6=average6,
            index7=average7,
            index8=average8,
            index9=average9,
            index10=average10,
            index11=average11,
            index12=average12,
            index13=average13,
            index14=average14,
            index15=average15,
            index16=average16,
            index17=average17,
            index18=average18,
            level='全体',
            depNum_id=dep_num,
            count=count,
            index19=sum0,
            index20=sum1,
            index21=sum2,
            index22=sum3,
            score=sum
        )
        # 上级
        xygbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum41 / count4 if count4 > 0 else 0),
            index2=(sum42 / count4 if count4 > 0 else 0),
            index3=(sum43 / count4 if count4 > 0 else 0),
            index4=(sum44 / count4 if count4 > 0 else 0),
            index5=(sum45 / count4 if count4 > 0 else 0),
            index6=(sum46 / count4 if count4 > 0 else 0),
            index7=(sum47 / count4 if count4 > 0 else 0),
            index8=(sum48 / count4 if count4 > 0 else 0),
            index9=(sum49 / count4 if count4 > 0 else 0),
            index10=(sum410 / count4 if count4 > 0 else 0),
            index11=(sum411 / count4 if count4 > 0 else 0),
            index12=(sum412 / count4 if count4 > 0 else 0),
            index13=(sum413 / count4 if count4 > 0 else 0),
            index14=(sum414 / count4 if count4 > 0 else 0),
            index15=(sum415 / count4 if count4 > 0 else 0),
            index16=(sum416 / count4 if count4 > 0 else 0),
            index17=(sum417 / count4 if count4 > 0 else 0),
            index18=(sum418 / count4 if count4 > 0 else 0),
            level='上级',
            depNum_id=dep_num,
            count=count4,
            score=sum4
        )
        # 同级
        xygbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum51 / count5 if count5 > 0 else 0),
            index2=(sum52 / count5 if count5 > 0 else 0),
            index3=(sum53 / count5 if count5 > 0 else 0),
            index4=(sum54 / count5 if count5 > 0 else 0),
            index5=(sum55 / count5 if count5 > 0 else 0),
            index6=(sum56 / count5 if count5 > 0 else 0),
            index7=(sum57 / count5 if count5 > 0 else 0),
            index8=(sum58 / count5 if count5 > 0 else 0),
            index9=(sum59 / count5 if count5 > 0 else 0),
            index10=(sum510 / count5 if count5 > 0 else 0),
            index11=(sum511 / count5 if count5 > 0 else 0),
            index12=(sum512 / count5 if count5 > 0 else 0),
            index13=(sum513 / count5 if count5 > 0 else 0),
            index14=(sum514 / count5 if count5 > 0 else 0),
            index15=(sum515 / count5 if count5 > 0 else 0),
            index16=(sum516 / count5 if count5 > 0 else 0),
            index17=(sum517 / count5 if count5 > 0 else 0),
            index18=(sum518 / count5 if count5 > 0 else 0),
            level='同级',
            depNum_id=dep_num,
            count=count5,
            score=sum5
        )
        # 下级
        xygbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum61 / count6 if count6 > 0 else 0),
            index2=(sum62 / count6 if count6 > 0 else 0),
            index3=(sum63 / count6 if count6 > 0 else 0),
            index4=(sum64 / count6 if count6 > 0 else 0),
            index5=(sum65 / count6 if count6 > 0 else 0),
            index6=(sum66 / count6 if count6 > 0 else 0),
            index7=(sum67 / count6 if count6 > 0 else 0),
            index8=(sum68 / count6 if count6 > 0 else 0),
            index9=(sum69 / count6 if count6 > 0 else 0),
            index10=(sum610 / count6 if count6 > 0 else 0),
            index11=(sum611 / count6 if count6 > 0 else 0),
            index12=(sum612 / count6 if count6 > 0 else 0),
            index13=(sum613 / count6 if count6 > 0 else 0),
            index14=(sum614 / count6 if count6 > 0 else 0),
            index15=(sum615 / count6 if count6 > 0 else 0),
            index16=(sum616 / count6 if count6 > 0 else 0),
            index17=(sum617 / count6 if count6 > 0 else 0),
            index18=(sum618 / count6 if count6 > 0 else 0),
            level='下级',
            depNum_id=dep_num,
            count=count6,
            score=sum6
        )


def jggbresult():
    """
    计算机关干部结果表
    :return:
    """
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
        dep_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('department_num', flat=True)[0]  # 被测评者的单位代码
        rank_num = Beiceping.objects.filter(IDcard=each_beiceping_id).values_list('rank_id_id', flat=True)[0]  # 被测评者的职级代码
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
        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09,
                    sum010, sum011, sum012, sum013, sum014, sum015, sum016, sum017, sum018]
        sum1_lst = [sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19,
                    sum110, sum111, sum112, sum113, sum114, sum115, sum116, sum117, sum118]
        sum2_lst = [sum21, sum22, sum23, sum24, sum25, sum26, sum27, sum28, sum29,
                    sum210, sum211, sum212, sum213, sum214, sum215, sum216, sum217, sum218]
        sum3_lst = [sum31, sum32, sum33, sum34, sum35, sum36, sum37, sum38, sum39,
                    sum310, sum311, sum312, sum313, sum314, sum315, sum316, sum317, sum318]
        sum4_lst = [sum41, sum42, sum43, sum44, sum45, sum46, sum47, sum48, sum49,
                    sum410, sum411, sum412, sum413, sum414, sum415, sum416, sum417, sum418]
        sum5_lst = [sum51, sum52, sum53, sum54, sum55, sum56, sum57, sum58, sum59,
                    sum510, sum511, sum512, sum513, sum514, sum515, sum516, sum517, sum518]
        sum6_lst = [sum61, sum62, sum63, sum64, sum65, sum66, sum67, sum68, sum69,
                    sum610, sum611, sum612, sum613, sum614, sum615, sum616, sum617, sum618]
        sum7_lst = [sum71, sum72, sum73, sum74, sum75, sum76, sum77, sum78, sum79,
                    sum710, sum711, sum712, sum713, sum714, sum715, sum716, sum717, sum718]

        if count0 > 0:
            for i in range(0, len(index_weight)):
                sum0 = sum0 + sum0_lst[i] * index_weight[i]
            sum0 = sum0 / count0
            # sum0 = (sum01 * zzpz_weight + sum02 * ddpx_weight + sum03 * gzsl_weight + sum04 * zznl_weight + sum05 * cxys_weight + sum06 * jyjs_weight + sum07 * fwtd_weight + sum08 * gfgl_weight + sum09 * bsxl_weight + sum010 * mbwc_weight + sum011 * tcyj_weight + sum012 * ljzl_weight) / count0
        if count1 > 0:
            for i in range(0, len(index_weight)):
                sum1 = sum1 + sum1_lst[i] * index_weight[i]
            sum1 = sum1 / count1
            # sum1 = (sum11 * zzpz_weight + sum12 * ddpx_weight + sum13 * gzsl_weight + sum14 * zznl_weight + sum15 * cxys_weight + sum16 * jyjs_weight + sum17 * fwtd_weight + sum18 * gfgl_weight + sum19 * bsxl_weight + sum110 * mbwc_weight + sum111 * tcyj_weight + sum112 * ljzl_weight) / count1
        if count2 > 0:
            for i in range(0, len(index_weight)):
                sum2 = sum2 + sum2_lst[i] * index_weight[i]
            sum2 = sum2 / count2
            # sum2 = (sum21 * zzpz_weight + sum22 * ddpx_weight + sum23 * gzsl_weight + sum24 * zznl_weight + sum25 * cxys_weight + sum26 * jyjs_weight + sum27 * fwtd_weight + sum28 * gfgl_weight + sum29 * bsxl_weight + sum210 * mbwc_weight + sum211 * tcyj_weight + sum212 * ljzl_weight) / count2
        if count3 > 0:
            for i in range(0, len(index_weight)):
                sum3 = sum3 + sum3_lst[i] * index_weight[i]
            sum3 = sum3 / count3
            # sum3 = (sum31 * zzpz_weight + sum32 * ddpx_weight + sum33 * gzsl_weight + sum34 * zznl_weight + sum35 * cxys_weight + sum36 * jyjs_weight + sum37 * fwtd_weight + sum38 * gfgl_weight + sum39 * bsxl_weight + sum310 * mbwc_weight + sum311 * tcyj_weight + sum312 * ljzl_weight) / count3
        if count4 > 0:
            for i in range(0, len(index_weight)):
                sum4 = sum4 + sum4_lst[i] * index_weight[i]
            sum4 = sum4 / count4
            # sum4 = (sum41 * zzpz_weight + sum42 * ddpx_weight + sum43 * gzsl_weight + sum44 * zznl_weight + sum45 * cxys_weight + sum46 * jyjs_weight + sum47 * fwtd_weight + sum48 * gfgl_weight + sum49 * bsxl_weight + sum410 * mbwc_weight + sum411 * tcyj_weight + sum412 * ljzl_weight) / count4
        if count5 > 0:
            for i in range(0, len(index_weight)):
                sum5 = sum5 + sum5_lst[i] * index_weight[i]
            sum5 = sum5 / count5
            # sum5 = (sum51 * zzpz_weight + sum52 * ddpx_weight + sum53 * gzsl_weight + sum54 * zznl_weight + sum55 * cxys_weight + sum56 * jyjs_weight + sum57 * fwtd_weight + sum58 * gfgl_weight + sum59 * bsxl_weight + sum510 * mbwc_weight + sum511 * tcyj_weight + sum512 * ljzl_weight) / count5
        if count6 > 0:
            for i in range(0, len(index_weight)):
                sum6 = sum6 + sum6_lst[i] * index_weight[i]
            sum6 = sum6 / count6
            # sum6 = (sum61 * zzpz_weight + sum62 * ddpx_weight + sum63 * gzsl_weight + sum64 * zznl_weight + sum65 * cxys_weight + sum66 * jyjs_weight + sum67 * fwtd_weight + sum68 * gfgl_weight + sum69 * bsxl_weight + sum610 * mbwc_weight + sum611 * tcyj_weight + sum612 * ljzl_weight) / count6
        if count7 > 0:
            for i in range(0, len(index_weight)):
                sum7 = sum7 + sum7_lst[i] * index_weight[i]
            sum7 = sum7 / count7
            # sum7 = (sum71 * zzpz_weight + sum72 * ddpx_weight + sum73 * gzsl_weight + sum74 * zznl_weight + sum75 * cxys_weight + sum76 * jyjs_weight + sum77 * fwtd_weight + sum78 * gfgl_weight + sum79 * bsxl_weight + sum710 * mbwc_weight + sum711 * tcyj_weight + sum712 * ljzl_weight) / count7

        sum = sum0 * index19_weight + sum1 * index20_weight + sum2 * index21_weight + sum3 * index22_weight + sum4 * index23_weight

        # 全体
        average1 = (sum01 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum11 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum21 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum31 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum41 * index23_weight / count4 if count4 > 0 else 0)

        average2 = (sum02 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum12 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum22 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum32 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum42 * index23_weight / count4 if count4 > 0 else 0)

        average3 = (sum03 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum13 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum23 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum33 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum43 * index23_weight / count4 if count4 > 0 else 0)

        average4 = (sum04 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum14 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum24 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum34 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum44 * index23_weight / count4 if count4 > 0 else 0)

        average5 = (sum05 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum15 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum25 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum35 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum45 * index23_weight / count4 if count4 > 0 else 0)

        average6 = (sum06 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum16 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum26 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum36 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum46 * index23_weight / count4 if count4 > 0 else 0)

        average7 = (sum07 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum17 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum27 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum37 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum47 * index23_weight / count4 if count4 > 0 else 0)

        average8 = (sum08 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum18 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum28 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum38 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum48 * index23_weight / count4 if count4 > 0 else 0)

        average9 = (sum09 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum19 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum29 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum39 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum49 * index23_weight / count4 if count4 > 0 else 0)

        average10 = (sum010 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum110 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum210 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum310 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum410 * index23_weight / count4 if count4 > 0 else 0)

        average11 = (sum011 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum111 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum211 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum311 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum411 * index23_weight / count4 if count4 > 0 else 0)

        average12 = (sum012 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum112 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum212 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum312 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum412 * index23_weight / count4 if count4 > 0 else 0)

        average13 = (sum013 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum113 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum213 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum313 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum413 * index23_weight / count4 if count4 > 0 else 0)

        average14 = (sum014 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum114 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum214 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum314 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum414 * index23_weight / count4 if count4 > 0 else 0)

        average15 = (sum015 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum115 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum215 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum315 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum415 * index23_weight / count4 if count4 > 0 else 0)

        average16 = (sum016 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum116 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum216 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum316 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum416 * index23_weight / count4 if count4 > 0 else 0)

        average17 = (sum017 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum117 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum217 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum317 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum417 * index23_weight / count4 if count4 > 0 else 0)

        average18 = (sum018 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum118 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum218 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum318 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum418 * index23_weight / count4 if count4 > 0 else 0)

        # 全体
        jggbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=average1,
            index2=average2,
            index3=average3,
            index4=average4,
            index5=average5,
            index6=average6,
            index7=average7,
            index8=average8,
            index9=average9,
            index10=average10,
            index11=average11,
            index12=average12,
            index13=average13,
            index14=average14,
            index15=average15,
            index16=average16,
            index17=average17,
            index18=average18,
            level='全体',
            depNum_id=dep_num,
            count=count,
            index19=sum0,
            index20=sum1,
            index21=sum2,
            index22=sum3,
            index23=sum4,
            score=sum
        )
        # 上级
        jggbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum51 / count5 if count5 > 0 else 0),
            index2=(sum52 / count5 if count5 > 0 else 0),
            index3=(sum53 / count5 if count5 > 0 else 0),
            index4=(sum54 / count5 if count5 > 0 else 0),
            index5=(sum55 / count5 if count5 > 0 else 0),
            index6=(sum56 / count5 if count5 > 0 else 0),
            index7=(sum57 / count5 if count5 > 0 else 0),
            index8=(sum58 / count5 if count5 > 0 else 0),
            index9=(sum59 / count5 if count5 > 0 else 0),
            index10=(sum510 / count5 if count5 > 0 else 0),
            index11=(sum511 / count5 if count5 > 0 else 0),
            index12=(sum512 / count5 if count5 > 0 else 0),
            index13=(sum513 / count5 if count5 > 0 else 0),
            index14=(sum514 / count5 if count5 > 0 else 0),
            index15=(sum515 / count5 if count5 > 0 else 0),
            index16=(sum516 / count5 if count5 > 0 else 0),
            index17=(sum517 / count5 if count5 > 0 else 0),
            index18=(sum518 / count5 if count5 > 0 else 0),
            level='上级',
            depNum_id=dep_num,
            count=count5,
            score=sum5
        )
        # 同级
        jggbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum61 / count6 if count6 > 0 else 0),
            index2=(sum62 / count6 if count6 > 0 else 0),
            index3=(sum63 / count6 if count6 > 0 else 0),
            index4=(sum64 / count6 if count6 > 0 else 0),
            index5=(sum65 / count6 if count6 > 0 else 0),
            index6=(sum66 / count6 if count6 > 0 else 0),
            index7=(sum67 / count6 if count6 > 0 else 0),
            index8=(sum68 / count6 if count6 > 0 else 0),
            index9=(sum69 / count6 if count6 > 0 else 0),
            index10=(sum610 / count6 if count6 > 0 else 0),
            index11=(sum611 / count6 if count6 > 0 else 0),
            index12=(sum612 / count6 if count6 > 0 else 0),
            index13=(sum613 / count6 if count6 > 0 else 0),
            index14=(sum614 / count6 if count6 > 0 else 0),
            index15=(sum615 / count6 if count6 > 0 else 0),
            index16=(sum616 / count6 if count6 > 0 else 0),
            index17=(sum617 / count6 if count6 > 0 else 0),
            index18=(sum618 / count6 if count6 > 0 else 0),
            level='同级',
            depNum_id=dep_num,
            count=count6,
            score=sum6
        )
        # 下级
        jggbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum71 / count7 if count7 > 0 else 0),
            index2=(sum72 / count7 if count7 > 0 else 0),
            index3=(sum73 / count7 if count7 > 0 else 0),
            index4=(sum74 / count7 if count7 > 0 else 0),
            index5=(sum75 / count7 if count7 > 0 else 0),
            index6=(sum76 / count7 if count7 > 0 else 0),
            index7=(sum77 / count7 if count7 > 0 else 0),
            index8=(sum78 / count7 if count7 > 0 else 0),
            index9=(sum79 / count7 if count7 > 0 else 0),
            index10=(sum710 / count7 if count7 > 0 else 0),
            index11=(sum711 / count7 if count7 > 0 else 0),
            index12=(sum712 / count7 if count7 > 0 else 0),
            index13=(sum713 / count7 if count7 > 0 else 0),
            index14=(sum714 / count7 if count7 > 0 else 0),
            index15=(sum715 / count7 if count7 > 0 else 0),
            index16=(sum716 / count7 if count7 > 0 else 0),
            index17=(sum717 / count7 if count7 > 0 else 0),
            index18=(sum718 / count7 if count7 > 0 else 0),
            level='下级',
            depNum_id=dep_num,
            count=count7,
            score=sum7
        )


def zsdwgbresult():
    """
    计算直属单位干部结果表
    :return:
    """
    # 直属单位干部指标权重表
    index_weight = []
    index_obj = zsdwgbIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])

    # 干部测评权重表
    index19_weight = GbCpWeight.objects.filter(code='010').values_list('weight', flat=True)[0]  # 直属单位校领导权重
    index20_weight = GbCpWeight.objects.filter(code='011').values_list('weight', flat=True)[0]  # 单位班子权重
    index21_weight = GbCpWeight.objects.filter(code='012').values_list('weight', flat=True)[0]  # 相关人员权重
    index22_weight = GbCpWeight.objects.filter(code='013').values_list('weight', flat=True)[0]  # 直属单位学院领导权重
    index23_weight = GbCpWeight.objects.filter(code='014').values_list('weight', flat=True)[0]  # 直属单位学院相关权重

    beiceping_id = zsdwgbTongji.objects.values_list('beiceping_id').distinct()  # 获取所有被测评人的id,并去重

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
        each_obj = zsdwgbTongji.objects.filter(beiceping=each_beiceping_id, giveup=0)  # 得到这个被测评人在统计表中的所有数据
        count = len(each_obj)  # 得到该被测评人的测评总数

        # 对每一个被测评者的每一条数据进行整理
        for j in range(0, count):
            cp_dep_num = each_obj[j].depNum_id  # 测评者的单位代码
            ceping_rank_id = each_obj[j].rankNum_id  # 测评者的职级代码

            # 直属单位校领导
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

            # 单位班子
            # if ceping_rank_id == '002' and '500' < cp_dep_num < '512':
            if ceping_rank_id == '002' and '400' < cp_dep_num:
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

            # 相关人员
            # if ceping_rank_id > '002' and (cp_dep_num < '300' or '500' < cp_dep_num < '512'):
            if ceping_rank_id > '002' and (cp_dep_num < '300' or '400' < cp_dep_num):
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

            # 直属单位学院领导
            # if ceping_rank_id == '002' and '300' < cp_dep_num < '500':
            if ceping_rank_id == '002' and '300' < cp_dep_num < '400':
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

            # 直属单位学院相关
            # if ceping_rank_id > '002' and '300' < cp_dep_num < '500':
            if ceping_rank_id > '002' and '300' < cp_dep_num < '400':
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

        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09,
                    sum010, sum011, sum012, sum013, sum014, sum015, sum016, sum017, sum018]
        sum1_lst = [sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19,
                    sum110, sum111, sum112, sum113, sum114, sum115, sum116, sum117, sum118]
        sum2_lst = [sum21, sum22, sum23, sum24, sum25, sum26, sum27, sum28, sum29,
                    sum210, sum211, sum212, sum213, sum214, sum215, sum216, sum217, sum218]
        sum3_lst = [sum31, sum32, sum33, sum34, sum35, sum36, sum37, sum38, sum39,
                    sum310, sum311, sum312, sum313, sum314, sum315, sum316, sum317, sum318]
        sum4_lst = [sum41, sum42, sum43, sum44, sum45, sum46, sum47, sum48, sum49,
                    sum410, sum411, sum412, sum413, sum414, sum415, sum416, sum417, sum418]
        sum5_lst = [sum51, sum52, sum53, sum54, sum55, sum56, sum57, sum58, sum59,
                    sum510, sum511, sum512, sum513, sum514, sum515, sum516, sum517, sum518]
        sum6_lst = [sum61, sum62, sum63, sum64, sum65, sum66, sum67, sum68, sum69,
                    sum610, sum611, sum612, sum613, sum614, sum615, sum616, sum617, sum618]
        sum7_lst = [sum71, sum72, sum73, sum74, sum75, sum76, sum77, sum78, sum79,
                    sum710, sum711, sum712, sum713, sum714, sum715, sum716, sum717, sum718]

        if count0 > 0:
            for i in range(0, len(index_weight)):
                sum0 = sum0 + sum0_lst[i] * index_weight[i]
            sum0 = sum0 / count0
        if count1 > 0:
            for i in range(0, len(index_weight)):
                sum1 = sum1 + sum1_lst[i] * index_weight[i]
            sum1 = sum1 / count1
        if count2 > 0:
            for i in range(0, len(index_weight)):
                sum2 = sum2 + sum2_lst[i] * index_weight[i]
            sum2 = sum2 / count2
        if count3 > 0:
            for i in range(0, len(index_weight)):
                sum3 = sum3 + sum3_lst[i] * index_weight[i]
            sum3 = sum3 / count3
        if count4 > 0:
            for i in range(0, len(index_weight)):
                sum4 = sum4 + sum4_lst[i] * index_weight[i]
            sum4 = sum4 / count4
        if count5 > 0:
            for i in range(0, len(index_weight)):
                sum5 = sum5 + sum5_lst[i] * index_weight[i]
            sum5 = sum5 / count5
        if count6 > 0:
            for i in range(0, len(index_weight)):
                sum6 = sum6 + sum6_lst[i] * index_weight[i]
            sum6 = sum6 / count6
        if count7 > 0:
            for i in range(0, len(index_weight)):
                sum7 = sum7 + sum7_lst[i] * index_weight[i]
            sum7 = sum7 / count7

        sum = sum0 * index19_weight + sum1 * index20_weight + sum2 * index21_weight + sum3 * index22_weight + sum4 * index23_weight

        # 全体
        average1 = (sum01 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum11 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum21 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum31 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum41 * index23_weight / count4 if count4 > 0 else 0)

        average2 = (sum02 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum12 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum22 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum32 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum42 * index23_weight / count4 if count4 > 0 else 0)

        average3 = (sum03 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum13 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum23 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum33 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum43 * index23_weight / count4 if count4 > 0 else 0)

        average4 = (sum04 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum14 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum24 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum34 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum44 * index23_weight / count4 if count4 > 0 else 0)

        average5 = (sum05 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum15 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum25 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum35 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum45 * index23_weight / count4 if count4 > 0 else 0)

        average6 = (sum06 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum16 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum26 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum36 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum46 * index23_weight / count4 if count4 > 0 else 0)

        average7 = (sum07 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum17 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum27 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum37 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum47 * index23_weight / count4 if count4 > 0 else 0)

        average8 = (sum08 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum18 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum28 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum38 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum48 * index23_weight / count4 if count4 > 0 else 0)

        average9 = (sum09 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum19 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum29 * index21_weight / count2 if count2 > 0 else 0) + \
                   (sum39 * index22_weight / count3 if count3 > 0 else 0) + \
                   (sum49 * index23_weight / count4 if count4 > 0 else 0)

        average10 = (sum010 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum110 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum210 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum310 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum410 * index23_weight / count4 if count4 > 0 else 0)

        average11 = (sum011 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum111 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum211 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum311 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum411 * index23_weight / count4 if count4 > 0 else 0)

        average12 = (sum012 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum112 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum212 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum312 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum412 * index23_weight / count4 if count4 > 0 else 0)

        average13 = (sum013 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum113 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum213 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum313 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum413 * index23_weight / count4 if count4 > 0 else 0)

        average14 = (sum014 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum114 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum214 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum314 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum414 * index23_weight / count4 if count4 > 0 else 0)

        average15 = (sum015 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum115 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum215 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum315 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum415 * index23_weight / count4 if count4 > 0 else 0)

        average16 = (sum016 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum116 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum216 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum316 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum416 * index23_weight / count4 if count4 > 0 else 0)

        average17 = (sum017 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum117 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum217 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum317 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum417 * index23_weight / count4 if count4 > 0 else 0)

        average18 = (sum018 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum118 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum218 * index21_weight / count2 if count2 > 0 else 0) + \
                    (sum318 * index22_weight / count3 if count3 > 0 else 0) + \
                    (sum418 * index23_weight / count4 if count4 > 0 else 0)

        # 全体
        zsdwgbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=average1,
            index2=average2,
            index3=average3,
            index4=average4,
            index5=average5,
            index6=average6,
            index7=average7,
            index8=average8,
            index9=average9,
            index10=average10,
            index11=average11,
            index12=average12,
            index13=average13,
            index14=average14,
            index15=average15,
            index16=average16,
            index17=average17,
            index18=average18,
            level='全体',
            depNum_id=dep_num,
            count=count,
            index19=sum0,
            index20=sum1,
            index21=sum2,
            index22=sum3,
            index23=sum4,
            score=sum
        )

        # 上级
        zsdwgbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum51 / count5 if count5 > 0 else 0),
            index2=(sum52 / count5 if count5 > 0 else 0),
            index3=(sum53 / count5 if count5 > 0 else 0),
            index4=(sum54 / count5 if count5 > 0 else 0),
            index5=(sum55 / count5 if count5 > 0 else 0),
            index6=(sum56 / count5 if count5 > 0 else 0),
            index7=(sum57 / count5 if count5 > 0 else 0),
            index8=(sum58 / count5 if count5 > 0 else 0),
            index9=(sum59 / count5 if count5 > 0 else 0),
            index10=(sum510 / count5 if count5 > 0 else 0),
            index11=(sum511 / count5 if count5 > 0 else 0),
            index12=(sum512 / count5 if count5 > 0 else 0),
            index13=(sum513 / count5 if count5 > 0 else 0),
            index14=(sum514 / count5 if count5 > 0 else 0),
            index15=(sum515 / count5 if count5 > 0 else 0),
            index16=(sum516 / count5 if count5 > 0 else 0),
            index17=(sum517 / count5 if count5 > 0 else 0),
            index18=(sum518 / count5 if count5 > 0 else 0),
            level='上级',
            depNum_id=dep_num,
            count=count5,
            score=sum5
        )

        # 同级
        zsdwgbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum61 / count6 if count6 > 0 else 0),
            index2=(sum62 / count6 if count6 > 0 else 0),
            index3=(sum63 / count6 if count6 > 0 else 0),
            index4=(sum64 / count6 if count6 > 0 else 0),
            index5=(sum65 / count6 if count6 > 0 else 0),
            index6=(sum66 / count6 if count6 > 0 else 0),
            index7=(sum67 / count6 if count6 > 0 else 0),
            index8=(sum68 / count6 if count6 > 0 else 0),
            index9=(sum69 / count6 if count6 > 0 else 0),
            index10=(sum610 / count6 if count6 > 0 else 0),
            index11=(sum611 / count6 if count6 > 0 else 0),
            index12=(sum612 / count6 if count6 > 0 else 0),
            index13=(sum613 / count6 if count6 > 0 else 0),
            index14=(sum614 / count6 if count6 > 0 else 0),
            index15=(sum615 / count6 if count6 > 0 else 0),
            index16=(sum616 / count6 if count6 > 0 else 0),
            index17=(sum617 / count6 if count6 > 0 else 0),
            index18=(sum618 / count6 if count6 > 0 else 0),
            level='同级',
            depNum_id=dep_num,
            count=count6,
            score=sum6
        )

        # 下级
        zsdwgbResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=(sum71 / count7 if count7 > 0 else 0),
            index2=(sum72 / count7 if count7 > 0 else 0),
            index3=(sum73 / count7 if count7 > 0 else 0),
            index4=(sum74 / count7 if count7 > 0 else 0),
            index5=(sum75 / count7 if count7 > 0 else 0),
            index6=(sum76 / count7 if count7 > 0 else 0),
            index7=(sum77 / count7 if count7 > 0 else 0),
            index8=(sum78 / count7 if count7 > 0 else 0),
            index9=(sum79 / count7 if count7 > 0 else 0),
            index10=(sum710 / count7 if count7 > 0 else 0),
            index11=(sum711 / count7 if count7 > 0 else 0),
            index12=(sum712 / count7 if count7 > 0 else 0),
            index13=(sum713 / count7 if count7 > 0 else 0),
            index14=(sum714 / count7 if count7 > 0 else 0),
            index15=(sum715 / count7 if count7 > 0 else 0),
            index16=(sum716 / count7 if count7 > 0 else 0),
            index17=(sum717 / count7 if count7 > 0 else 0),
            index18=(sum718 / count7 if count7 > 0 else 0),
            level='下级',
            depNum_id=dep_num,
            count=count7,
            score=sum7
        )


def xybzresult():
    """
    计算学院班子结果表
    :return:
    """
    # 学院班子指标权重表
    index_weight = []
    index_obj = xybzIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])

    beiceping_id = xybzTongji.objects.values_list('beiceping_id').distinct()  # 获取所有被测评人的id,并去重

    # 处理每一个被测评人的分数
    for i in range(0, len(beiceping_id)):
        sum0 = sum01 = sum02 = sum03 = sum04 = sum05 = sum06 = sum07 = sum08 = sum09 = sum010 = sum011 = sum012 = 0
        each_beiceping_id = beiceping_id[i][0]  # 得到每一个被测评人的id
        each_obj = xybzTongji.objects.filter(beiceping=each_beiceping_id, giveup=0)  # 得到这个被测评人在统计表中的所有数据
        count = len(each_obj)  # 得到该被测评人的测评总数

        # 对每一个被测评者的每一条数据进行整理
        for j in range(0, count):
            # 每一项指标进行累加
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

        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09, sum010, sum011, sum012]

        if count > 0:
            for i in range(0, len(index_weight)):
                sum0 = sum0 + sum0_lst[i] * index_weight[i]
            sum0 = sum0 / count
            # sum0 = (sum01 * fzsl_weight + sum02 * cxys_weight + sum03 * kxjc_weight + sum04 * mzgl_weight + sum05 * mbgl_weight + sum06 * tsld_weight + sum07 * nhjs_weight + sum08 * fzts_weight) / count
            average1 = sum01 / count
            average2 = sum02 / count
            average3 = sum03 / count
            average4 = sum04 / count
            average5 = sum05 / count
            average6 = sum06 / count
            average7 = sum07 / count
            average8 = sum08 / count
            average9 = sum09 / count
            average10 = sum010 / count
            average11 = sum011 / count
            average12 = sum012 / count

        # 将结果添加到学院班子统计表中
        xybzResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=average1,
            index2=average2,
            index3=average3,
            index4=average4,
            index5=average5,
            index6=average6,
            index7=average7,
            index8=average8,
            index9=average9,
            index10=average10,
            index11=average11,
            index12=average12,
            count=count,
            score=sum0
        )


def zsdwbzresult():
    """
    计算直属单位班子结果表
    :return:
    """
    # 直属单位班子指标权重表
    index_weight = []
    index_obj = zsdwbzIndexWeight.objects.filter(index__isnull=False, weight__isnull=False).values()
    for i in range(0, len(index_obj)):
        index_weight.append(index_obj[i]['weight'])

    # 领导班子测评权重表
    index19_weight = BzCpWeight.objects.filter(code='001').values_list('weight', flat=True)[0]  # 校领导权重
    index20_weight = BzCpWeight.objects.filter(code='002').values_list('weight', flat=True)[0]  # 党政负责人权重
    index21_weight = BzCpWeight.objects.filter(code='003').values_list('weight', flat=True)[0]  # 单位职工师生代表权重

    beiceping_id = zsdwbzTongji.objects.values_list('beiceping_id').distinct()  # 获取所有被测评人的id,并去重

    # 处理每一个被测评人的分数
    for i in range(0, len(beiceping_id)):
        count0 = count1 = count2 = 0
        sum0 = sum01 = sum02 = sum03 = sum04 = sum05 = sum06 = sum07 = sum08 = sum09 = sum010 = sum011 = sum012 = 0
        sum1 = sum11 = sum12 = sum13 = sum14 = sum15 = sum16 = sum17 = sum18 = sum19 = sum110 = sum111 = sum112 = 0
        sum2 = sum21 = sum22 = sum23 = sum24 = sum25 = sum26 = sum27 = sum28 = sum29 = sum210 = sum211 = sum212 = 0

        each_beiceping_id = beiceping_id[i][0]  # 得到每一个被测评人的id
        each_obj = zsdwbzTongji.objects.filter(beiceping=each_beiceping_id, giveup=0)  # 得到这个被测评人在统计表中的所有数据
        count = len(each_obj)  # 得到该被测评人的测评总数

        # 对每一个被测评者的每一条数据进行整理
        for j in range(0, count):
            cp_dep_num = each_obj[j].depcode_id  # 测评者的单位代码
            ceping_rank_id = each_obj[j].rankNum_id  # 测评者的职级代码

            # 校领导
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

            # 党政负责人
            if ceping_rank_id == '002':
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

            # 单位职工师生代表
            # 此处有疑问
            if ceping_rank_id > '002' and cp_dep_num < '016' or cp_dep_num > '300':
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

        sum0_lst = [sum01, sum02, sum03, sum04, sum05, sum06, sum07, sum08, sum09, sum010, sum011, sum012]
        sum1_lst = [sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19, sum110, sum111, sum112]
        sum2_lst = [sum21, sum22, sum23, sum24, sum25, sum26, sum27, sum28, sum29, sum210, sum211, sum212]

        if count0 > 0:
            for i in range(0, len(index_weight)):
                sum0 = sum0 + sum0_lst[i] * index_weight[i]
            sum0 = sum0 / count0
            # sum0 = (sum01 * fzsl_weight + sum02 * cxys_weight + sum03 * kxjc_weight + sum04 * yxjz_weight + sum05 * mbwc_weight + sum06 * fwbz_weight + sum07 * zhxy_weight + sum08 * fzts_weight) / count0
        if count1 > 0:
            for i in range(0, len(index_weight)):
                sum1 = sum1 + sum1_lst[i] * index_weight[i]
            sum1 = sum1 / count1
            # sum1 = (sum11 * fzsl_weight + sum12 * cxys_weight + sum13 * kxjc_weight + sum14 * yxjz_weight + sum15 * mbwc_weight + sum16 * fwbz_weight + sum17 * zhxy_weight + sum18 * fzts_weight) / count1
        if count2 > 0:
            for i in range(0, len(index_weight)):
                sum2 = sum2 + sum2_lst[i] * index_weight[i]
            sum2 = sum2 / count2
            # sum2 = (sum21 * fzsl_weight + sum22 * cxys_weight + sum23 * kxjc_weight + sum24 * yxjz_weight + sum25 * mbwc_weight + sum26 * fwbz_weight + sum27 * zhxy_weight + sum28 * fzts_weight) / count2

        sum = sum0 * index19_weight + sum1 * index20_weight + sum2 * index21_weight

        # 全体
        average1 = (sum01 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum11 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum21 * index21_weight / count2 if count2 > 0 else 0)

        average2 = (sum02 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum12 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum22 * index21_weight / count2 if count2 > 0 else 0)

        average3 = (sum03 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum13 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum23 * index21_weight / count2 if count2 > 0 else 0)

        average4 = (sum04 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum14 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum24 * index21_weight / count2 if count2 > 0 else 0)

        average5 = (sum05 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum15 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum25 * index21_weight / count2 if count2 > 0 else 0)

        average6 = (sum06 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum16 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum26 * index21_weight / count2 if count2 > 0 else 0)

        average7 = (sum07 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum17 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum27 * index21_weight / count2 if count2 > 0 else 0)

        average8 = (sum08 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum18 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum28 * index21_weight / count2 if count2 > 0 else 0)

        average9 = (sum09 * index19_weight / count0 if count0 > 0 else 0) + \
                   (sum19 * index20_weight / count1 if count1 > 0 else 0) + \
                   (sum29 * index21_weight / count2 if count2 > 0 else 0)

        average10 = (sum010 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum110 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum210 * index21_weight / count2 if count2 > 0 else 0)

        average11 = (sum011 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum111 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum211 * index21_weight / count2 if count2 > 0 else 0)

        average12 = (sum012 * index19_weight / count0 if count0 > 0 else 0) + \
                    (sum112 * index20_weight / count1 if count1 > 0 else 0) + \
                    (sum212 * index21_weight / count2 if count2 > 0 else 0)

        # 全体
        zsdwbzResult.objects.create(
            beiceping_id=each_beiceping_id,
            index1=average1,
            index2=average2,
            index3=average3,
            index4=average4,
            index5=average5,
            index6=average6,
            index7=average7,
            index8=average8,
            index9=average9,
            index10=average10,
            index11=average11,
            index12=average12,
            count=count,
            index19=sum0,
            index20=sum1,
            index21=sum2,
            score=sum
        )