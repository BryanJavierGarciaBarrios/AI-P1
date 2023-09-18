# -- coding: utf-8 --
import datetime, locale
locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now() #Muestra fecha, hora, segundos y microsegundos

print(fecha)
print("Year:",fecha.year,"Month:",fecha.month,"Day:",fecha.day)

print(fecha.strftime("%A")) #Utilizando strftime, podemos mostrar el dia de la semana

#Nota strftime
#fecha.strftime(%letra)
"""D�a de la semana abreviado: %a "
"D�a de la semana completo: %A "
"Mes abreviado: %b "
"Mes abreviado: %B "
"Fecha completa: %c "
"D�a del mes (01 - 31): %d "
"D�a/hora/a�o: %D "
"D�a del mes (1 - 31): %e "
"A�o en dos d�gitos: %g "
"A�o en cuatro d�gitos: %G "
"Mes abreviado: %h "
"Hora (00 - 23): %H "
"Hora (01 - 12): %I "
"D�a del a�o: %j "
"Mes del 01 al 12: %m "
"Minuto: %M "
"Salto de l�nea: %n"
"AM o PM: %p "
"Hora + AM o PM: %r"
"Hora y minutos: %R"
"Segundos: %S"
"Tabulaci�n: %t"
"Hora, minutos y segundos: %T"
"D�a de la semana (n�mero): %u"
"Semana del a�o (empieza en domingo): %U"
"Semana del a�o(Condiciones especiales): %V"
"Semana del a�o (empieza en lunes): %W"
"D�a de la semana (empieza en domingo): %w"
"D�a/mes/a�o de dos d�gitos: %x"
"Hora/minutos/segundos: %X"
"A�o corto: %y"
"A�o largo: %Y"""