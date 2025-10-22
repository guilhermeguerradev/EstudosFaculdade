from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entities.nota import Nota

class Participante:

    def __init__(self, id, codigo, razaoSocial, cnpj, nota: 'Nota' = None):
        self.__id = id
        self.__codigo = codigo
        self.__razaoSocial = razaoSocial
        self.__cnpj = cnpj
        if nota:
            self.__notas = [nota]
        else:
            self.__notas = []  # Lista de Notas

    # ---------- Getters ----------
    def getId(self):
        return self.__id
    
    def getCodigo(self):
        return self.__codigo
    
    def getRazaoSocial(self):
        return self.__razaoSocial
    
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

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def adicionarNota(self, nota: 'Nota'):
        self.__notas.append(nota)


