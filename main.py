# -*- coding: UTF-8 -*-

import random
import StaffClass
import Count_DayNumbers


if __name__ == '__main__':

    name_list = ['郭俊华', 'ltt', 'yird']
    daynumber = Count_DayNumbers.Count_DayNumbers()
    daynumber.count_daynumbers()


    duty_info = StaffClass.StaffClass()
    duty_info.name_list = name_list
    duty_info.StaffInfoDict(name_list)
    duty_info.daynumber = daynumber

    duty_info.duty_list = []

    print duty_info.daynumber
    print duty_info.duty_info_dict