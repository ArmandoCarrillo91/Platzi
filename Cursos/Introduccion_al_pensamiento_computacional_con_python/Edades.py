nombre_1 = input('Escribe tu nombre :')
edad_1 = int(input('Escribe tu edad :'))

nombre_2 = input('Escribe tu nombre :')
edad_2 = int(input('Escribe tu edad :'))

if edad_1 > edad_2:
    print(nombre_1 + ' Tiene mayor edad que ' + nombre_2)
elif edad_2 > edad_1:
    print(nombre_2 + ' Tiene mayor edad que ' + nombre_1)
else:
    pass