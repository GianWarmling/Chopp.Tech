from datetime import datetime

def saudacao():
    hora = datetime.now(tz=None)

    if hora.hour >= 5 and hora.hour < 12:
        print("Bom Dia!")

    elif hora.hour >= 12 and hora.hour < 18:
        print("Boa Tarde!")

    else:
        print("Boa Noite!")

def Create(cliente):
        with open ('chopp_tech.txt', 'a') as arquivo:
            arquivo.write(str(cliente)+ '\n')

def Chopp(chopp):
     with open('chopp_tech.txt', 'a') as arquivo:
         arquivo.write(str(chopp)+ '\n')

def relatorio():
     with open('chopp_tech.txt', 'r') as arquivo:
          print(arquivo.read())



def FazerCheckout(cliente):
    index = 0
    flag = 0
    chave = index

    try:
        with open("chopp_tech.txt", "r") as arquivo:
            lines = arquivo.readlines()

            posicao = 1

            with open("chopp_tech.txt", "w") as arquivo:
                for line in lines:
                    if posicao != chave:
                        arquivo.write(line)

                    posicao += 1
        print("Pedido Deletado")
        
    except:
        print("Erro de Sistema")
                   