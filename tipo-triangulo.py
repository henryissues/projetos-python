n1 = float(input('Digite um lado do triangulo: '))
n2 = float(input('Digite o outro lado: '))
n3 = float(input('Digite o restante: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Poderá formar um triangulo')
    if n1 == n2 == n3:
        print('Será um triangulo equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Será um triangulo Isósceles')
    else:
        print('Será um triangulo escaleno')
else:
    print('Não poderá formar um triangulo')