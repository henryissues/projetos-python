nome = str(input('Digite um nome completo: ')).strip()

esp = nome.find(' ')
primeiro = nome[0:esp] #vai do primeiro ate o primeiro espaco
qtd = len(nome)
espf = nome.rfind(' ')
ultimo = nome[espf:qtd] #vai do ultimo espaco ate o final

print('Primeiro nome: {}'.format(primeiro))
print('Ultimo nome: {}'.format(ultimo))