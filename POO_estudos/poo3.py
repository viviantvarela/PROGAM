class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def total(self):
       return self._preco 

    @total.setter
    def total(self, preco):
        if preco < 0:
            raise ValueError("[Erro - Valor Negativo]: O preço não pode ser um valor negativo!")
        self._preco = preco

p = Produto(10)
print(p.total)