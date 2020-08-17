import random


def gen_pwd():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '^', '/', '(', ')']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    

    caracteres = mayusculas + minusculas + simbolos + numeros

    pwd = []

    for i in range(9):
        caracter_random = random.choice(caracteres)
        pwd.append(caracter_random)

    pwd = ''.join(pwd)
    return pwd


def run():
    pwd = gen_pwd()
    print('Tu contrasena es: ' + pwd)
    

if __name__ == '__main__':
    run()