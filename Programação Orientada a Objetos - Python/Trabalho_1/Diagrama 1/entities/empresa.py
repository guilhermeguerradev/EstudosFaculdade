from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities.nota import Nota

class Empresa:

    def __init__(self, id, codigo, razaoSocial, endereco, cnpj, nota: 'Nota' = None):
        self.__id = id
        self.__codigo = codigo
        self.__razaoSocial = razaoSocial
        self.__endereco = endereco
        self.__cnpj = cnpj
        if nota:
            self.__notas = [nota]
        else:
            self.__notas = []

    # ---------- Getters ----------
    def getId(self):
        return self.__id
    
    def getCodigo(self):
        return self.__codigo
    
    def getRazaoSocial(self):
        return self.__razaoSocial
    
    def getEndereco(self):
        return self.__endereco
    
    def getCnpj(self):
        return self.__cnpj
    
    def getNotas(self):
        return self.__notas
    
    # ---------- Setters ----------


    def setId(self, id):
        self.__id = id

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setRazaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj
    
    def adicionarNota(self, nota: 'Nota'):
        self.__notas.append(nota)

