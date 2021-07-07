import random

def jogar():
    print(" ")
    print("————————————————————————————————————————————————————————————————————————")
    print("SEJA BEM-VINDO AO JOGO SUPER SECRETO SECRETÍSSIMO DE ADVINHAÇÃO SECRETA!")
    print("————————————————————————————————————————————————————————————————————————")
    print(" ")

    numero_secreto = random.randrange(1,31)
    tentativas = 0
    pontos = 500

    print(" ")
    print("Em qual nível você deseja jogar?")
    nivel = int(input("Digite 1 para FÁCIL, 2 para MÉDIO e 3 para DIFÍCIL!"))

    if(nivel == 1):
        tentativas = 10
    if(nivel == 2):
        tentativas = 6
    if(nivel == 3):
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print(" ")
        print("——— Tentativa {} de {}. ———".format(rodada, tentativas))
        chute_str = input("Chute um número de 1 a 30!")
        perdeu = rodada == 10

    # aqui a variável está especificamente com o nome "str" para sabermos que
    # ela é uma string, que precisa ser convertida em número inteiro para o
    # código funcionar.

        print("Você chutou o número " + chute_str + ".")
        chute = int(chute_str)

    # aqui o chute em formato string está sendo
    # convertido em número inteiro com a função "int".

        acertou      = chute == numero_secreto
        chutou_maior = chute > numero_secreto
        chutou_menor = chute < numero_secreto
        maior_que_trinta = chute > 30
        menor_que_um = chute < 1
        continuar = 1
        parar = 0

        if(maior_que_trinta or menor_que_um):
            print("Por favor, insira um número válido.")
            continue

    # continue é usado para sair dessa interação e "repetir" o restante do código,
    # um break mais leve.

        if(acertou):
            print(" ")
            print("Parabéns! Você ganhou e fez {} pontos!".format(pontos))
            jogar_novamente = int(input("Deseja jogar novamente? Digite 1 para SIM e 2 para NÃO."))
            if (jogar_novamente == 1):
                jogar()
            if (jogar_novamente == 2):
                break
        else:
            if(chutou_maior):
                print("Você errou, que peninha! O número secreto é menor do que o seu chute.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            if (chutou_menor):
                print("Você errou, que peninha! O número secreto é maior do que o seu chute.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            if (perdeu):
                print(" ")
                print("Você perdeu! :(")

    print(" ")
    print("FIM DE JOGO!")

if (__name__ == "__main__"):
    jogar()