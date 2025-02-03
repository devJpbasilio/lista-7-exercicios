"""
Soma de números naturais
Peça um número ao usuário e calcule a soma de todos os números naturais até ele
(exemplo: para 5, a soma seria 1 + 2 + 3 + 4 + 5 = 15).
"""
numero = int(input("Digite um número: "))
soma = sum(range(1, numero + 1))
print(f"A soma dos números de 1 a {numero} é {soma}")