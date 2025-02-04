import random


def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhacao!")
    print("Tente adivinhar o número entre 1 e 100.")

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("O número deve estar entre 1 e 100. Tente novamente!")
            elif palpite < numero_secreto:
                print("Tente um número maior!")
            elif palpite > numero_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns!! Você acertou em {tentativas} tentativas!")
                acertou = True
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


adivinhe_o_numero()