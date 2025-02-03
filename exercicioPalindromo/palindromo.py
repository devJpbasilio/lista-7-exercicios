
"""
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igual de frente para trás, ignorando espaços e maiúsculas).
"""
print("Jogo Palíndromo")
palavra = input("\nDigite uma palavra: ").replace(' ', '').lower()

if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")