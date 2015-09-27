# diaprogramador
# Determina el dia de la semana en que ocurrira el dia del programador segun el año dado
# corre en Python 3

# JNC

# Uso:
# python diaprogramador.py año

# Para su correcto funcionamiento, debe instalarse la libreria GoSlate desde PyPi:
#    pip install goslate
# Esta libreria accede al servicio Google Translate, por lo que es necesario
# estar conectado a internet para que funcione

# NOTA: google translate traduce 'september' como 'setiembre', que segun la
# RAE, es valido: http://www.como-se-escribe.com/setiembre-o-septiembre/


# Bibliotecas a usar
import sys, datetime as dt, goslate as g

# El año viene dado por un argumento dado al programa en la consola
try:
    year = int(sys.argv[1])

    # Parametro interno del numero de dia del año en que se celebra el dia del
    # programador. Cambiar segun se considere necesario
    dia = 256

    # Dia de hoy, sin horas/minutos/segundos
    hoy = dt.datetime.strptime(dt.datetime.now().strftime('%Y%m%d'),'%Y%m%d')

    # Calculo el dia del programador con base en 1 de enero del año dado, mas numero de dias definido
    diaprogramador = dt.datetime.strptime("{year}0101".format(year=year),'%Y%m%d') + dt.timedelta(dia - 1)

    # El diccionario define el comportamiento, depende el año
    # Hay 3 (en realidad 5) comportamientos:
    # * 'pre2002': previo a 2002
    # * 'hoy': a dia de hoy
    # * 'difHoy': los dos ultimos incisos van de la mano porque la diferencia gramatical de los enunciados es minima
    #   - antes del dia de hoy (que se desglosa en antes del 2009 (ruso) y el resto de los casos)
    #   - luego del dia de hoy

    # difHoy traduce todo a ruso o español depende el año (previo a 2009 o no).
    # Las variables preposicion y tiempo se ajustan depende si el año esta en el pasado o el futuro
    # Las variables year y day salen directamente como numneros del diaprogramador calculado
    # Las variables weekday y month salen tambien de ahi pero usando primero datetime.strftime
    #   saco los nombres comunes, y los traduzco a español primero.
    #   Resulta que mi sistema tiene el locale en ingles y si eso pasa en cualquier
    #   maquina... mejor primero homogeneizo a español para evitarle confusiones a
    #   Google Translate

               # Si año < 2002 , aun no habia dia del programador
    mensaje = {'pre2002' : "En esa fecha aún no se celebraba el día del programador",
               # Si dia de ejecucion = dia del programador, mensaje en presente
               'hoy'     : "¡El día del programador se celebra hoy! ¡Felicidades!",
               # Si dia de ejecucion > dia del programador, mensaje en preterito
               # Si dia de ejecucion < dia del programador, mensaje en futuro
               # Si año < 2009 , mensaje en ruso, solo habia dia de programador en Rusia
               'difHoy'  : g.Goslate().translate("El día del programador {preposicion} {year} se celebr{tiempo} el {weekday} {day} de {month}".format(preposicion="en" if diaprogramador < hoy else "del año",
                                                                                                                                                      tiempo="ó" if diaprogramador < hoy else "ará",
                                                                                                                                                      year=year,
                                                                                                                                                      day=diaprogramador.day,
                                                                                                                                                      weekday=g.Goslate().translate(diaprogramador.strftime('%A'),'es'),
                                                                                                                                                      month=g.Goslate().translate(diaprogramador.strftime('%B'),'es') ),
                                                 'ru' if year < 2009 else 'es')}

    # Imprimir el mensaje con base en el año dado se define la llave del diccionario anterior
    print (mensaje['pre2002' if year < 2002 else ('hoy' if diaprogramador == hoy else 'difHoy')])

except ValueError:
    print("USO: python diaprogramador.py año")
