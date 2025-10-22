from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entities.nota import Nota
    from entities.produto import Produto

class ItemNota:

    def __init__(self, id, vrUnitario, quantidade, nota: 'Nota', produto : 'Produto'):
        self.__id = id
        self.__vrUnitario = vrUnitario
        self.__quantidade = quantidade
        self.__nota = nota
        self.__produto = produto



    # ---------- Getters ----------
    def getId(self):
        return self.__id
    
    def getVrUnitario(self):
        return self.__vrUnitario
    
    def getQuantidade(self):
        return self.__quantidade
    
    def getNota(self):
        return self.__nota
    
    def getProduto(self):
        return self.__produto
    
    # ---------- Setters ----------

    def setId(self, id):
        self.__id = id

    def setVrUnitario(self, vrUnitario):
        self.__vrUnitario = vrUnitario

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    def setNota(self, nota):
        self.__nota = nota

    def setProduto(self, produto):
        self.__produto = produto
    


    def getTotal(self):
        return self.getQuantidade() * self.getVrUnitario()


