import random

jogo = ['pedra', 'papel', 'tesoura']
palavra_sorteada = random.choice(jogo)
palavra_escolhida = input('Escolha pedra, papel ou tesoura: ')

regras = {
    'pedra':'tesoura',
    'tesoura':'papel',
    'papel':'pedra'
}

print('Ada Wong escolheu: {}'.format(palavra_sorteada))

if palavra_escolhida == palavra_sorteada:
    print('Empate!')
elif regras[palavra_escolhida] == palavra_sorteada:
    print('Você ganhou!')
else:
    print('Ada Wong ganhou!')