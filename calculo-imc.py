h = float(input('Qual sua altura?(em m) '))
m = float(input('Qual é sua massa? '))

imc = m/(h*h)
print('Seu IMC é igual a {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')