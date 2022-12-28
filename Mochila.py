from Item import Item

class Mochila:
    def __init__(mochila, capacidade: int):
        mochila.capacidade: int = capacidade
        mochila.itens: Item = []
        mochila.adaptacao = None

    def __str__(self) -> str:
        for i in self.itens:
            print(i)
        return f'\nA adaptação do cromossomo é: {self.adaptacao}\nO peso total da mochila é: {self.pesoTotal()}'

    def capacidadeAtual(self):
        capacidade: int = 0
        for i in self.itens:
            capacidade = capacidade + i.pesoAtual()
        
        return capacidade

    def valorTotal(self):
        valor = 0
        for i in self.itens:
            valor = valor + i.valorAtual()
        
        self.adaptacao = round(valor,2)

        return round(valor,2)
    
    def pesoTotal(self):
        peso = 0
        for i in self.itens:
            peso = peso + i.pesoAtual()
    
        return round(peso,2)

    def adaptacao(self):        
        return self.adaptacao