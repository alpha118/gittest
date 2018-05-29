import calendar
import time
import StaffClass

class Count_DayNumbers():
    def __init__(self):
        pass

    def count_daynumbers(self):
        currentTime = time.localtime()
        currentYear = currentTime[0]
        currentMonth = currentTime[1]

        if currentMonth == 12:
            Year = currentYear + 1
            Month = 1
            self.dayNumbers = calendar.monthrange(Year, Month)[1]
        else:
            Month = currentMonth + 1
            self.dayNumbers = calendar.monthrange(currentYear, Month)[1]

if __name__ == '__main__':
    a = Count_DayNumbers()
    a.count_daynumbers()
    print a.dayNumbers
