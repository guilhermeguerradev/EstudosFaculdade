
class Pessoa:
    def __init__(self, id, nome, cpf, dataNascimento, email, endereco, telefone, identidade):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNascimento = dataNascimento
        self.__email = email
        self.__endereco = endereco
        self.__telefone = telefone
        self.__identidade = identidade

    # Getters
    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getDataNascimento(self):
        return self.__dataNascimento

    def getEmail(self):
        return self.__email

    def getEndereco(self):
        return self.__endereco

    def getTelefone(self):
        return self.__telefone

    def getIdentidade(self):
        return self.__identidade

    # Setters
    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def setEmail(self, email):
        self.__email = email

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def setIdentidade(self, identidade):
        self.__identidade = identidade
