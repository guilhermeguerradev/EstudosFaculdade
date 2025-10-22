from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id, nome, cpf, dataNascimento, email, endereco, telefone, identidade,
                 matricula, anoInicio, semestreInicio, situacao):

        super().__init__(id, nome, cpf, dataNascimento, email, endereco, telefone, identidade)

        self.__matricula = matricula
        self.__anoInicio = anoInicio
        self.__semestreInicio = semestreInicio


        self.__diarios = []

        self.__situacoes = [situacao]
        situacao.adicionarAluno(self)

    # ---------- Getters ----------
    def getMatricula(self):
        return self.__matricula

    def getAnoInicio(self):
        return self.__anoInicio

    def getSemestreInicio(self):
        return self.__semestreInicio

    def getSituacoes(self):
        return self.__situacoes

    def getDiarios(self):
        return self.__diarios

    # ---------- Métodos de associação ----------
    def adicionarSituacao(self, situacao):
        if situacao not in self.__situacoes:
            self.__situacoes.append(situacao)
            situacao.adicionarAluno(self)

    def removerSituacao(self, situacao):
        if situacao in self.__situacoes:
            self.__situacoes.remove(situacao)
            situacao.removerAluno(self)

    def adicionarDiario(self, diario):
        if diario not in self.__diarios:
            self.__diarios.append(diario)
            diario.setAluno(self)

    def removerDiario(self, diario):
        if diario in self.__diarios:
            self.__diarios.remove(diario)
            diario.setAluno(None)
