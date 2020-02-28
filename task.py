# import math
# from datetime import date


def firstrun():
    return "success"


def getArea(radius):
    PI = 3.142
    return int(PI * (radius*radius)*100)/100


def getElementList(aList):

    resList = []
    resList.append(aList[0])
    resList.append(aList[-1])

    return resList


def daysBWdates(date1, date2):

    delta = abs(date2 - date1)

    return delta.days
