from entities.empresa import Empresa
from entities.participante import Participante
from entities.itemNota import ItemNota

class Nota:


    def __init__(self, id, data, numero, itemNota : ItemNota, empresa : Empresa, participante : Participante):
        self.__id = id
        self.__data = data
        self.__numero = numero
        self.__empresa = empresa  # Associação com Empresa
        self.__participante = participante  # Associação com Participante
        self.__itensNota = [itemNota]

        


    # ---------- Getters ----------
    def getId(self):
        return self.__id
    
    def getData(self):
        return self.__data
    
    def getNumero(self):
        return self.__numero
    
    def getEmpresa(self):
        return self.__empresa
    
    def getParticipante(self):
        return self.__participante
    
    def getItensNota(self):
        return self.__itensNota

    # ---------- Setters ----------
    def setId(self, id):
        self.__id = id

    def setData(self, data):
        self.__data = data
    
    def setNumero(self, numero):
        self.__numero = numero
    
    def setEmpresa(self, empresa: Empresa):
        self.__empresa = empresa

    def setParticipante(self, participante: Participante):
        self.__participante = participante



    def addItemNota(self, itemNota: ItemNota):
        self.__itensNota.append(itemNota)
    



    def getVrTotal(self):
        total = 0
        for item in self.__itensNota:
            total += item.getTotal()
        
        return total



