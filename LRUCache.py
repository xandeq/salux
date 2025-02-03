from collections import OrderedDict

class CacheLRU:
    def __init__(self, limite: int):
        self.armazenamento = OrderedDict()
        self.limite = limite

    def buscar(self, chave: int) -> int:
        if chave not in self.armazenamento:
            return -1
        self.armazenamento.move_to_end(chave)
        return self.armazenamento[chave]

    def inserir(self, chave: int, valor: int) -> None:
        if chave in self.armazenamento:
            self.armazenamento.move_to_end(chave)
        elif len(self.armazenamento) >= self.limite:
            self.armazenamento.popitem(last=False)
        self.armazenamento[chave] = valor


if __name__ == "__main__":
    cache = CacheLRU(2)
    
    cache.inserir(1, 1)
    cache.inserir(2, 2)

    print(cache.buscar(1))

    cache.inserir(3, 3)

    print(cache.buscar(2))

    cache.inserir(4, 4)

    print(cache.buscar(1))
    print(cache.buscar(3))
    print(cache.buscar(4))
