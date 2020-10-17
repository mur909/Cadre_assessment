from Renyuan.models import Ceping


def update_code(zhiwu, num, code):
    info = Ceping.objects.filter(zhiwu=zhiwu).values('IDcard', 'department__number', 'label')
    for i in info:
        if int(i['department__number'][0]) in num:
            if str(i['label']) == 'None':
                Ceping.objects.filter(IDcard=i['IDcard']).update(label=code)
            else:
                label = str(i['label']) + code
                Ceping.objects.filter(IDcard=i['IDcard']).update(label=label)

def is_repetition(value):
    lst = []
    print(value.index(value[0:3:4]))

is_repetition(value='J001H002J001')