class Turma:
    def __init__(self, id, descricao, ano, semestre, professor, instituicao, disciplina):
        self.__id = id
        self.__descricao = descricao
        self.__ano = ano
        self.__semestre = semestre
        self.__professor = professor
        self.__instituicao = instituicao
        self.__disciplina = disciplina
        self.__diarios = []  # 0..*

        # Cria os vínculos nos dois lados
        professor.adicionarTurma(self)
        instituicao.adicionarTurma(self)
        disciplina.adicionarTurma(self)

    # ---------- Getters ----------
    def getId(self):
        return self.__id

    def getDescricao(self):
        return self.__descricao

    def getAno(self):
        return self.__ano

    def getSemestre(self):
        return self.__semestre

    def getProfessor(self):
        return self.__professor

    def getInstituicao(self):
        return self.__instituicao

    def getDisciplina(self):
        return self.__disciplina

    def getDiarios(self):
        return self.__diarios

    # ---------- Setters ----------
    def setId(self, id):
        self.__id = id

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setAno(self, ano):
        self.__ano = ano

    def setSemestre(self, semestre):
        self.__semestre = semestre

    def setProfessor(self, professor):
        self.__professor = professor
        professor.adicionarTurma(self)

    def setInstituicao(self, instituicao):
        self.__instituicao = instituicao
        instituicao.adicionarTurma(self)

    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina
        disciplina.adicionarTurma(self)

    # ---------- Turma ↔ Diário ----------
    def adicionarDiario(self, diario):
        if diario not in self.__diarios:
            self.__diarios.append(diario)
            diario.setTurma(self)

    def removerDiario(self, diario):
        if diario in self.__diarios:
            self.__diarios.remove(diario)
            diario.setTurma(None)
