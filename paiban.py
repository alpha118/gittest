# -*- coding: GBK -*-
import calendar
import random
import time


def count_daynumbers():
    currentTime = time.localtime()
    currentYear = currentTime[0]
    currentMonth = currentTime[1]

    if currentMonth == 12:
        Year = currentYear + 1
        Month = 1
        dayNumbers = calendar.monthrange(Year, Month)[1]
    else:
        Month = currentMonth + 1
        dayNumbers = calendar.monthrange(currentYear, Month)[1]

    return dayNumbers


def count_dutycheckstartdate(date):
    if date <= 7:
        dutyCheckStartDate = 1
    else:
        dutyCheckStartDate = date - 7
    return dutyCheckStartDate


def count_dutycheckenddate(date):
    if date == 1:
        dutyCheckEndDate = 1
    else:
        dutyCheckEndDate = date - 1
    return dutyCheckEndDate


def standbyduty():
    dictStandby = {}
    l = []
    for key in dictPeople.keys():
        l = l + [dictPeople[key]['Times']]
    minTimes = min(l)
    for y in dictPeople.keys():
        if dictPeople[y]['Times'] == minTimes:
            dictStandby[y] = dictPeople[y]
    return dictStandby

dictPeople = {0: {'Name': '���俵', 'Times': 0},
              1: {'Name': '������', 'Times': 0},
              2: {'Name': '�ƴ�ҫ', 'Times': 0},
              3: {'Name': '�¼���', 'Times': 0},
              4: {'Name': '���ε�', 'Times': 0},
              5: {'Name': '��ӱ��', 'Times': 0},
              6: {'Name': '������', 'Times': 0},
              7: {'Name': '������', 'Times': 0},
              8: {'Name': '������', 'Times': 0},
              9: {'Name': '������', 'Times': 0},
              10: {'Name': '������', 'Times': 0},
              11: {'Name': '����', 'Times': 0}
              }
listDuty = []

# �����¸��µ��·ݣ������¸����м���
dayNumbers = count_daynumbers()

# �����Ű��
for date in range(1, dayNumbers + 1, 1):

    dutyCheckStartDate = count_dutycheckstartdate(date)
    dutyCheckEndDate = count_dutycheckenddate(date)
    dictStandby = standbyduty()

    for people in dictStandby:
        dutyPeople = random.choice(standbyduty().keys())
        if dictStandby[dutyPeople]['Name'] in listDuty[dutyCheckStartDate: dutyCheckEndDate + 2]:
            dutyPeople = random.choice(standbyduty().keys())
        else:
            listDuty.append(dictStandby[dutyPeople]['Name'])
            break

    dictPeople[dutyPeople]['Times'] = dictPeople[dutyPeople]['Times'] + 1

for key in listDuty:
    print key
