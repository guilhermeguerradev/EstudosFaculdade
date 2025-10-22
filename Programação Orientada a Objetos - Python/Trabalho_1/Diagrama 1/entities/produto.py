from entities.itemNota import ItemNota

class Produto:

    def __init__(self, id, codigo, descricao, itemNota : ItemNota=None):
        self.__id = id
        self.__codigo = codigo
        self.__descricao = descricao
        if itemNota:
            self.__itensNota = [itemNota]
        else:
            self.__itensNota = []  # Lista de Notas

    # ---------- Getters ----------

    def getId(self):
        return self.__id
    
    def getCodigo(self):
        return self.__codigo
    
    def getDescricao(self):
        return self.__descricao
    
    def getItensNota(self):
        return self.__itensNota
    
    # ---------- Setters ----------
    
    def setId(self, id):
        self.__id = id

    def setCodigo(self, codigo):
        self.__codigo = codigo
    
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def addItemNota(self, itemNota : ItemNota):
        self.__itensNota.append(itemNota)
    
