#-*- coding: utf-8 -*-
import sys, datetime, locale

DAY_TO_EVAL = 256
nameDayES = [u"lunes", u"martes", u"miércoles", u"jueves", u"viernes", u"sábado", u"domingo"]
nameMonthES = [u"", u"enero", u"febrero", u"marzo", u"abril", u"mayo", u"junio", u"julio", u"agosto", u"septiembre", u"octubre", u"noviembre", u"diciembre"]
nameDayRU = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
nameMonthRU = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "ноябрь", "Декабрь"]

def whatMessagePD(YEAR):
    daySelected = datetime.date(YEAR, 1, 1) + datetime.timedelta(DAY_TO_EVAL - 1)
    if YEAR < 2002:
        return u"Todavía no se celebraba el día del programador"
    if YEAR < 2009:
        return "День Разработчик состоялась в %s, %s, %s %s" % (YEAR, nameDayRU[daySelected.weekday()], daySelected.day, nameMonthRU[daySelected.month])
    if daySelected < datetime.date.today():
        return u"El día del programador en %s se celebró el %s %s de %s" % (YEAR, nameDayES[daySelected.weekday()], daySelected.day, nameMonthES[daySelected.month])
    if datetime.date.today() == daySelected:
        return u"El día del programador se celebra hoy! Felicidades!"
    return u"El día del programador del año %s se celebrará el %s %s de %s" % (YEAR, nameDayES[daySelected.weekday()], daySelected.day, nameMonthES[daySelected.month])

if len(sys.argv) == 2:
    try:
        print whatMessagePD(int(sys.argv[1]))
    except:
        print u"Se necesita un parámetro válido"
else:
    print u"Se necesita un solo parámetro"
