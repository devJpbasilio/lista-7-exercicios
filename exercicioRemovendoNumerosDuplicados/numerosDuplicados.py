import random


def remover_duplicatas(lista):
    return list(set(lista))


#numeros = random.choices(range(1, 100), k=30)
numeros = [random.randint(1, 100) for _ in range(30)]
print("Lista gerada:")
print(numeros)

print("\nRemovendo os números duplicados:")
print(remover_duplicatas(numeros))