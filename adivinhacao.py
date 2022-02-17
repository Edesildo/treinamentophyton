import  random

def jogar():
        print ("**************************")
        print ("Bem vindo ao jogo de Advinhação")
        print ("**************************")

        numero_secreto= random.randrange(1,101)
        total_de_tentativas = 0
        pontos = 1000

        print("Qual nível de dificuldade")
        print("(1) Facil  (2) Médio e (3) Difícil")

        nivel= int(input("Defina 1 nivel :"))

        if(nivel == 1 ):
            total_de_tentativas = 20
        elif(nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5


        for rodada in range(1,total_de_tentativas + 1) :
            print("Tentativas:  {} de {} " .format(rodada,total_de_tentativas))
            chute_str = input("Digite um numero entre 1 e 100: ")
            print("Você digitou ", chute_str)
            chute = int(chute_str)

            if(chute < 1 or chute > 100):
                print("Voce deveria digita um numero entre 1 e 100!!")
                continue

            acertou = chute == numero_secreto
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto

            if(acertou):
                print("Você acertou e fez {} pontos".format(pontos))
                break
            else:
                if(maior):
                    print("Você errou! O seu chute foi maior do que o numero secreto")
                elif(menor):
                    print("Você errou! O seu chute foi menor do que o numero secreto")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos
                    print("FIM DO JOGO")



if(__name__ == "__main__"):
    jogar()