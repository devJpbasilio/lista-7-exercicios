import random


def soma_tulpa(numeros):
    return sum(numeros)

t = random.choices(range(1, 100), k=10)
print(t)
print(f"Lista de somas de 10 elementos: {soma_tulpa(t)}")