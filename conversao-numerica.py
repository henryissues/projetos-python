n1 = int(input('Digite um número: '))
n2 = int(input(('Escolha uma função para conversão: \n' 
'1: Binário \n' \
'2: Octal \n' \
'3: Hexadecimal \n')))

if n2 == 1:
    binario = bin(n1)[2:]
    print(binario)
elif n2 == 2:
    octal = oct(n2)[2:]
    print(octal)
elif n2 == 3:
    hexadecimal = hex(n1)[2:]
    print(hexadecimal)
else:
    print('Número inválido. Tente Novamente!')