from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
ano_atual = int(date.today().year)
idade = ano_atual - ano
print('O Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Será Mirim')
elif idade <= 14:
    print('Será Infantil')
elif idade <= 19:
    print('Será Junior')
elif idade <= 25:
    print('Será Sênior')
else:
    print('Será Master')