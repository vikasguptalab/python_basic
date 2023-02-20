#!/usr/bin/python

def getTime():
    import time;

    localtime = time.localtime(time.time())
    return "Local current time :", localtime


# print(getTime())


def getCalender():
    # !/usr/bin/python
    import calendar
    try:
        calendarYear = int(input("Enter the Year: "))
        calendarMonth = int(input("Enter the Month Number: "))
    except ValueError:
        return "Invalid Value Received"

    if calendarMonth == '':
        return "Missing Year"

    cal = calendar.month(calendarYear, calendarMonth)
    return "Here is the calendar:" + cal


# print(getCalender())

def timeDateTime():
    from datetime import datetime, date, time, timezone
    # Using datetime.combine()
    d = date(2023, 2, 2)
    t = time();

    return datetime.combine(d, t)


print(timeDateTime())
