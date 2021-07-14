import random

def jogar():

    mensagem_inicial()
    palavra_secreta = gera_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_chutadas = []
    pular_linha()
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()

        letras_chutadas.append(chute)
        mostra_chute(letras_chutadas)
        verifica_tamanho(chute)

        if(chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)
            pular_linha()

        print(letras_acertadas)

        #enforcou ou acertou?
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if(acertou):
        pular_linha()
        print("Parabéns, você ganhou!")
    else:
        pular_linha()
        print("Você perdeu! A palavra era {}.".format(palavra_secreta))

    jogar_novamente()

                                     #————funções abaixo————
def pular_linha():
    print("")

def mensagem_inicial():
    pular_linha()
    print("———————————————————————————————————————————————————————————————————")
    print("SEJA BEM-VINDO AO JOGO SUPER SECRETO SECRETÍSSIMO DE FORCA SECRETA!")
    print("———————————————————————————————————————————————————————————————————")

def gera_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Chute UMA letra:")
    pular_linha()
    chute = chute.strip().upper()
    return chute

def verifica_tamanho(chute):
    while True:
        if len(chute) <= 1:
            break
        else:
            print("POR FAVOR, CHUTE APENAS UMA LETRA!")
            break

def chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1

def mostra_chute(letras_chutadas):
    texto = ""
    for index in range(0, len(letras_chutadas)):
        texto = texto + " " + letras_chutadas[index]
    print("Você chutou as letras:", texto);


def jogar_novamente():
    escolha = int(input("Deseja jogar novamente? Digite 1 para SIM ou 2 para NÃO."))
    if (escolha == 1):
        jogar()
    else:
        pular_linha()
        print("FIM DE JOGO!")
        raise SystemExit

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()




