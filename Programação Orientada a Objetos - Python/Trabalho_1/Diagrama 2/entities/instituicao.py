class Instituicao:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao
        self.__turmas = []  # 0..*

    # ---------- Getters ----------
    def getId(self):
        return self.__id

    def getDescricao(self):
        return self.__descricao

    def getTurmas(self):
        return self.__turmas

    # ---------- Setters ----------
    def setId(self, id):
        self.__id = id

    def setDescricao(self, descricao):
        self.__descricao = descricao

    # ---------- Instituição ↔ Turma ----------
    def adicionarTurma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)
            turma.setInstituicao(self)

    def removerTurma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            if turma.getInstituicao() == self:
                turma.setInstituicao(None)
