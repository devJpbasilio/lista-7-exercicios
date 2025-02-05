import random

"""
Descrição: Crie uma função que recebe uma lista de números e
retorna outra lista contendo apenas os números pares.
"""

def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]


lista = random.sample(range(1, 101), 30)
print(f"Lista gerada com números aleatóris: {lista}")

print("\nFiltrando os números pares:")
print(filtrar_pares(lista))