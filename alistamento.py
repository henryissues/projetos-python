from datetime import date
ano = int(input('Diga seu ano de nascimento: '))
ano_atual = int(date.today().year)
idade = ano_atual - ano
sexo = str(input('Diga seu sexo(M ou F): '))

if sexo == 'M':
    if idade < 18:
        tempo = 18 - idade
        print('Ainda não está na hora de se alistar')
        ano_ideal = ano_atual + tempo
        print('Voce poderá se alistar em {}.'.format(ano_ideal))
    elif idade == 18:
        print('Está na hora de se alistar')
    else:
        tempo = idade - 18
        print('Já passou da hora de se alistar')
        print('Já passou {} anos que poderia ter se alistado'.format(tempo))
elif sexo == 'F':
    print('Não é necessário o alistamento militar obrigatório.')
else:
    print('Insira um sexo válido')