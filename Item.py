class Item:
    def __init__(item, valor: int, peso: int, nome: str, prioridade: int, fracao: float = 1):
        item.peso = peso
        item.valorTotal = valor
        item.nome = nome
        item.prioridade = prioridade
        item.fracao = fracao

    def __str__(self) -> str:
        prioridade = None
        if self.prioridade == 1:
            prioridade = "Baixa"
        elif self.prioridade == 2:
            prioridade = "Média"
        elif self.prioridade == 3:
            prioridade = "Alta"
        return f'Item: {self.nome}\tPeso inteiro: {self.peso} \tPeso fracionado: {self.pesoAtual()}\tValor total: {self.valorTotal}  \tValor atual: {self.valorAtual()}  \tPorcentagem adquirida: {round(self.fracao*100,2)}%\tPrioridade: {prioridade}'

    def valorAtual(self):
        return round(self.valorTotal * self.fracao,2)

    def pesoAtual(self):
        return round(self.peso * self.fracao,2)