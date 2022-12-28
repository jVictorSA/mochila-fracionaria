import random
import copy
from Item import Item
from Mochila import Mochila

def inicializaMochila(mochila: Mochila, itens: Item = []):
    itensDestaMochila = copy.deepcopy(itens)

    # Insere o máximo de itens aleatórios na mochila
    while mochila.capacidadeAtual() < mochila.capacidade:
        i = random.randint(0, len(itensDestaMochila)-1)
        item = copy.deepcopy(itensDestaMochila[i])
        mochila.itens.append(item)
    
    # Remove randomicamente da mochila a fim de que ela não exceda sua capacidade
    # Dessa forma não haverão indivíduos monstros
    while mochila.capacidadeAtual() > mochila.capacidade:
        i = random.randint(0, len(mochila.itens)-1)
        deducao = round(random.uniform(0.1,mochila.itens[i].fracao),2)
        if mochila.itens[i].fracao - deducao <= 0:
            mochila.itens[i].fracao = 0.1
        else:    
            mochila.itens[i].fracao = round(mochila.itens[i].fracao - deducao,2)

    return mochila

def criaPop(popSize: int, capacidade: int, itens: Item = []):
    pop: Mochila = []
    for i in range(popSize):
        mochila = Mochila(capacidade)
        mochila = inicializaMochila(mochila, itens)
        mochila.valorTotal()
        pop.append(mochila)

    return pop

def mutacao(mochila: Mochila):
    fracao = 0
    i = random.randint(0,len(mochila.itens)-1)

    if mochila.itens[i].prioridade == 1:
        if mochila.itens[i].fracao > 0.3:
            fracao = round(random.uniform(0.1, 0.3),2)
        else:
            fracao = round(random.uniform(0.1, mochila.itens[i].fracao),2)
    elif mochila.itens[i].prioridade == 3:
        if mochila.itens[i].fracao > 0.7:
            fracao = round(random.uniform(mochila.itens[i].fracao, 1),2)
        else:    
            fracao = round(random.uniform(0.7, 1),2)
    else:
        fracao = round(random.uniform(0.1, 1),2)

    if mochila.capacidadeAtual() - mochila.itens[i].pesoAtual() + (mochila.itens[i].peso * fracao) > mochila.capacidade:
        excesso = mochila.capacidadeAtual() - mochila.itens[i].pesoAtual() + (mochila.itens[i].peso * fracao) - mochila.capacidade
        excesso = excesso/mochila.itens[i].peso

        fracao = fracao - excesso
    
    mochila.itens[i].fracao = fracao
    mochila.valorTotal()
    return mochila

def cruzamento(pai: Mochila, mae: Mochila):
    menorItens = len(pai.itens) if len(pai.itens) < len(mae.itens) else len(mae.itens)

    if menorItens > 2:
        menorItens = menorItens - 1

    corte = random.randint(1, menorItens)

    filho1: Mochila = Mochila(pai.capacidade)
    filho2: Mochila = Mochila(pai.capacidade)

    for i in range(corte):
        item = copy.deepcopy(pai.itens[i])
        filho1.itens.append(item)

    for i in range(len(mae.itens)-corte):
        item = copy.deepcopy(mae.itens[i+corte])
        filho1.itens.append(item)

    for i in range(corte):
        item = copy.deepcopy(mae.itens[i])
        filho2.itens.append(item)

    for i in range(len(pai.itens)-corte):
        item = copy.deepcopy(pai.itens[i+corte])
        filho2.itens.append(item)

    while filho1.capacidadeAtual() > filho1.capacidade:
        i = random.randint(0, len(filho1.itens)-1)
        deducao = 0
        if filho1.itens[i].prioridade == 3:
            deducao = round(random.uniform(0.1,filho1.itens[i].fracao),2)
        else:
            deducao = round(random.uniform(filho1.itens[i].fracao, 1),2)
        
        if filho1.itens[i].fracao - deducao <= 0:
            filho1.itens[i].fracao = 0.1
        else:    
            filho1.itens[i].fracao = round(filho1.itens[i].fracao - deducao,2)

    while filho2.capacidadeAtual() > filho2.capacidade:
        i = random.randint(0, len(filho2.itens)-1)

        deducao = 0
        if filho2.itens[i].prioridade == 3:
            deducao = round(random.uniform(0.1, 0.3),2)
        else:
            deducao = round(random.uniform(0.7, 1),2)

        if filho2.itens[i].fracao - deducao <= 0:
            filho2.itens[i].fracao = 0.1
        else:    
            filho2.itens[i].fracao = round(filho2.itens[i].fracao - deducao,2)

    filho1.valorTotal()
    filho2.valorTotal()

    return filho1, filho2

def ordenaPop(pop: Mochila = []):
    pop.sort(key=lambda x: x.adaptacao, reverse = True)

def selecao(pop: Mochila = []):
    i,j = 0, 0
    while i == j:
        i = random.randint(0, len(pop)-1)
        j = random.randint(0, len(pop)-1)

    return i, j

def substituicao(pop: Mochila = [], filhos: Mochila = []):
    novaPop: Mochila = []
    i = 0
    j = 0
    while len(novaPop) != len(pop):
        if pop[i].valorTotal() > filhos[j].valorTotal():
            novaPop.append(pop[i])
            i = i + 1
        else:
            novaPop.append(filhos[j])
            j = j + 1

    return novaPop

def printaPop(pop: Mochila = []):
    for i in range(len(pop)):
        for j in pop[i].itens:
            print(j)
        print(f'Valor total: {pop[i].valorTotal()}\tPeso total: {pop[i].pesoTotal()}')
        print("--------------------------------------------------------------------------------------------")

def printAdaptacao(pop: Mochila = []):
    count = 1
    for i in pop:
        print(f'Cromossomo: {count} - {i.adaptacao} de adaptação')        
        print("--------------------------------------------------------------------------------------------")
        count = count + 1

def seleciona2cromossomos(pop: Mochila = []):
    i,j = 0, 0
    while i == j:
        i = random.randint(0, len(pop)-1)
        j = random.randint(0, len(pop)-1)
    
    return i, j

def selecaoeCruzamento(pop: Mochila = [], filhos: Mochila = []):
    for i in range(0, len(pop)-1, 2):
        j, k = selecao(pop)
        filhos[i], filhos[i+1] = cruzamento(pop[j], pop[k])

    return filhos


def solucao(capacidade, geracoes: int, populacaoMax: int, itens: Item = []):
    pop: Mochila = []
    filhos: Mochila = []

    pop = criaPop(populacaoMax, capacidade, itens)
    filhos = criaPop(populacaoMax, capacidade, itens)

    k = 0
    while k < geracoes:
        print(f'######################################## GERAÇÃO {k+1} ########################################')
        i , j = seleciona2cromossomos(pop)
        pop[i] = mutacao(pop[i])
        pop[j] = mutacao(pop[j])
        
        filhos = selecaoeCruzamento(pop, filhos)
        
        ordenaPop(pop)
        ordenaPop(filhos)
        pop = substituicao(pop, filhos)
        printAdaptacao(pop)
        k = k + 1

    print("\n\n######################################################################### MELHOR CROMOSSOMO #####################################################################")
    print(f'{pop[0]}')
    print("######################################################################### MELHOR CROMOSSOMO #####################################################################\n\n")
