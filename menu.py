from controller import saudacao, Create, Chopp, relatorio, FazerCheckout

def menu():

    menu = 1

    while menu != 0:
        saudacao()

        var = int(input("Informe sua Idade para prosserguirmos: "))
        if var < 18:
            print("Venda proibida para menores de 18 anos!!!")
            menu = 0
            
        elif var >= 18:

            opcao = int(input("O que você deseja?\nDigite:\n1-Para Cadastro:\n2-Fazer Pedido:\n3-Leitura:\n4-Alteração:\n5-Deletar:\n>>> "))

            match opcao:
                case 1:
                    pessoa = {}
                    pessoa['Nome'] = input("Digite seu Nome: ")
                    pessoa['Telefone'] = input("Digite seu Telefone: ")
                    pessoa['CPF'] = input("Digite seu CPF: ")
                    pessoa['Endereço'] = input("Digite seu Endereço: ")
                    Create(pessoa)

                case 2:
                    pedido = input("Qual opção você deseja?\nDigite:\nP-Chopp Pilsen:\nV-Chopp de Vinho:\n>>> ")

                    if pedido == 'P':
                    
                        cardapio = input("Você deseja Growler(Digite G) R$ 20,00 Valor p/ Litro:\nVocê deseja Barril(Digite B) R$ 500,00 p/ Barril:\n>>> ")
                        quantidade = int(input("Qual a quantidade que você deseja? "))
                        
                        if cardapio == 'G':
                            valor = 20
                            conta = valor * (quantidade)
                        else:
                            valor = 500
                            conta = valor * (quantidade)


                    elif pedido == 'V':

                        cardapio = input("Você deseja Growler(Digite G)R$ 25,00:\nVocê deseja Barril(Digite B)R$ 550,00:\n>>> ")
                        quantidade = int(input("Qual a quantidade que você deseja? "))

                        if cardapio == 'G':
                            valor = 25
                            conta = valor * (quantidade)
                        else:
                            valor = 550
                            conta = valor * (quantidade)
 
                    car = {}
                    car['Chopp'] = (pedido)
                    car['Produto'] = (cardapio)
                    car['Quantidade'] = (quantidade)
                    car['R$'] = (conta)
                    

                    Chopp(car)

                case 3:
                    relatorio()

                case 4:
                    pass

                case 5:
                    FazerCheckout()

            menu = int(input("O que você deseja?\nDigite 0 para Sair!\nDigite 1 para Continuar!\n"))

menu()