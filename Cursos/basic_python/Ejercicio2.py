dolares = input('Cuantos dolares tienes?: ')
dolares = float(dolares)
valor_dolar = 0.045
peso = dolares / valor_dolar
peso = round(peso,2)
peso = str(peso)
print('Tienes $' + peso + ' Pesos')