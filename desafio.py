#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import strftime
from sys import argv, exit

def isLeap(year):
	return ((year % 400) == 0) or (((year % 4) == 0) and ((year % 100) != 0))

def dayOfWeek(day, month, year):
    days = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return days[(year + year/4 - year/100 + year/400 + t[month-1] + day) % 7]

year = 0
if (len(argv) == 2):
    try:
        year = int(argv[1])
    except:
        print "Año no válido"
        exit(1)
else:
    print "Debe ingresar el año"
    exit(0)

currD, currM, currY = [int(x) for x in strftime("%d,%m,%Y").split(",")]
(day, month) = (256, 0)
months = [31, 29 if isLeap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsNames = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

m = 0
while day > months[m]:
    day -= months[m]
    m += 1
    month = m

dayName = dayOfWeek(day, month+1, year)

if year < 2002:
    print "Aún no se celebra el día del programador"
elif year < 2009:
    #segun google translator
    print "Он по-прежнему отмечается программист"
elif year <= currY:
    if day == currD and currM-1 == month and currY == year:
        print "El día del programador se celebra hoy! Felicidades!"
    else:
        print "El día del programador en %d se celebró el %s %d de %s" % (year, dayName, day, monthsNames[month])
else:
    print "El día del programador del año %d se celebrará el %s %d de %s" % (year, dayName, day, monthsNames[month])
