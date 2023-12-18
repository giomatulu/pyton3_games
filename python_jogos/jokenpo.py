import random

# CPU
lista = ["pedra", "papel", "tesoura"]
computador = random.choice(lista)

# jogador
jogador = input("*.*.*BEM-VINDO AO JOKENPÔ!*.*.* \nEscolha pedra, papel ou tesoura:").lower()

if jogador != "pedra" and jogador != "papel" and jogador != "tesoura":
    print("Escolha uma opção válida e tente novamente!")
    exit()
        
# empate 
if jogador == "pedra" and computador == "pedra" or \
jogador == "papel" and computador == "papel" or \
jogador == "tesoura" and computador == "tesoura":
    print("EMPATE!")
    exit()
        
# jogos - pedra < papel, papel < tesoura, tesoura < pedra
    
if jogador == "pedra" and computador == "papel" \
or jogador == "papel" and computador == "tesoura" \
or jogador == "tesoura" and computador == "pedra":
    print("PERDEU! O computador tinha escolhido: " + computador + "!")
else:
    print("GANHOU! O computador tinha escolhido: " + computador + "!")
        