# -- coding: utf-8 --
import datetime, locale
locale.setlocale(locale.LC_ALL, "es-ES")

fecha = datetime.datetime.now() #Muestra fecha, hora, segundos y microsegundos

print(fecha)
print("Year:",fecha.year,"Month:",fecha.month,"Day:",fecha.day)

print(fecha.strftime("%A")) #Utilizando strftime, podemos mostrar el dia de la semana

#Nota strftime
#fecha.strftime(%letra)
"""Día de la semana abreviado: %a "
"Día de la semana completo: %A "
"Mes abreviado: %b "
"Mes abreviado: %B "
"Fecha completa: %c "
"Día del mes (01 - 31): %d "
"Día/hora/año: %D "
"Día del mes (1 - 31): %e "
"Año en dos dígitos: %g "
"Año en cuatro dígitos: %G "
"Mes abreviado: %h "
"Hora (00 - 23): %H "
"Hora (01 - 12): %I "
"Día del año: %j "
"Mes del 01 al 12: %m "
"Minuto: %M "
"Salto de línea: %n"
"AM o PM: %p "
"Hora + AM o PM: %r"
"Hora y minutos: %R"
"Segundos: %S"
"Tabulación: %t"
"Hora, minutos y segundos: %T"
"Día de la semana (número): %u"
"Semana del año (empieza en domingo): %U"
"Semana del año(Condiciones especiales): %V"
"Semana del año (empieza en lunes): %W"
"Día de la semana (empieza en domingo): %w"
"Día/mes/año de dos dígitos: %x"
"Hora/minutos/segundos: %X"
"Año corto: %y"
"Año largo: %Y"""