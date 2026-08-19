valor = float(input('Quantos reais vc gastou? '))
m = int(input('Qual vai ser a forma de pagamento? \n' \
'1 - A vista \n' \
'2 - Cartao \n' \
'3 - 2x no Cartao \n' \
'4 - 3x ou mais no Cartao \n'))

if m == 1:
    valor = valor * 0.9
    print('O valor final é {} reais'.format(valor))
elif m == 2:
    valor = valor * 0.95
    print('O valor total é {} reais'.format(valor))
elif m == 3:
    print('O valor total é {} reais'.format(valor))
elif m == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor = valor * 1.2
    valor_parcela = valor/parcelas
    print('O valor toal é {} reais com parcelas de {} reais.'.format(valor, valor_parcela))
else:
    print('Insira um número válido.')