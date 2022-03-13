
class Vendas:
    def __init__(self, produto, valor, qtd):
        self._produto = produto
        self._valor = valor 
        self._qtd = qtd 

    def info(self):
        print(self._produto)
        print("Valor: ", self._valor)
        print("Quantidade: ", self._qtd)

    @property
    def produto(self):
        return self._produto

    @property
    def valor(self):
        return self._valor

    @property
    def qtd(self):
        return self._qtd
