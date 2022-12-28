import Item
import AlgGenetico

if __name__ == '__main__':
    print("\n\tALGORITMO GENÉTICO PARA RESOLVER O PROBLEMA DA MOCHILA FRACIONÁRIA\n")
    geracoes = 10
    capacidade = 10
    popMax = 12
    itens : Item.Item = []

    itens.append(Item.Item(15.0, 2.0, "calça", 1))
    itens.append(Item.Item(3.0, 1.0, "camisa", 2))
    itens.append(Item.Item(14.0, 9.0, "cerveja", 2))
    itens.append(Item.Item(5.0, 1.0, "boné", 3))
    itens.append(Item.Item(25.0, 4.0, "ouro", 3))

    usando = True
    while usando:
        print("\tDigite 1 para ver a lista de itens pré-selecionados para o problema")
        print("\tDigite 2 para inserir um item na lista de itens do problema")
        print("\tDigite 3 para alterar a prioridade de um item na lista")
        print("\tDigite 4 encontrar uma solução para o problema")
        print("\tDigite 5 para alterar o numero de gerações máxima do algoritmo genético")
        print("\tDigite 6 para alterar o numero de cromossomos da população do algoritmo genético")
        print("\tDigite 7 para alterar a capacidade das mochilas do problema")
        print("\tDigite 8 para ver a configuração atual do algoritmo genético")
        print("\tDigite 9 para sair")
        opcao = int(input())
        
        if opcao == 1:
            print("\n#################################################################################################################################################################")
            for i in itens:
                print(i)
            print("#################################################################################################################################################################\n")
        elif opcao == 2:
            print("Digite o nome do item:")
            nome = input()
            print("Digite o peso total do item:")
            peso = round(float(input()),2)
            print("Digite o valor total do item:")
            valor = round(float(input()),2)
            print("Digite a prioridade do item")
            print("Digite 1 para prioridade baixa:")
            print("Digite 2 para prioridade média:")
            print("Digite 3 para prioridade alta:")
            prioridade = int(input())
            
            itens.append(Item.Item(valor, peso, nome, prioridade))
        elif opcao == 3:
            pass
        elif opcao == 4:
            AlgGenetico.solucao(capacidade, geracoes, popMax, itens)
        elif opcao == 5:
            print("Digite o novo numero máximo de gerações:")
            geracoes = int(input())
        elif opcao == 6:
            print("O numero máximo da população deve ser um número par maior ou igual a 4.\nDigite o novo numero máximo da população:")
            entrada = int(input())
            if entrada % 2 == 0 and entrada >= 4:
                popMax = entrada
            else:
                print("Numero inválido!")

        elif opcao == 7:
            print("Digite a nova capacidade das mochilas do problema:")
            capacidade = int(input())
        elif opcao == 8:
            print(f'\n\t# Numero de gerações: {geracoes}\n\t# Tamanho da população: {popMax}\n\t# Capacidade das mochilas: {capacidade}\n')
        elif opcao == 9:
            usando = False
        else:
            print("Este número não é uma opção valida!")
            continue

    print("\n\nObrigado por usar o sistema")