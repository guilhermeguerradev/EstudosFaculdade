class Curso:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao
        self.__disciplinas = []   # 0..*
        self.__professores = []   # N:N

    # ---------- Getters ----------
    def getId(self):
        return self.__id

    def getDescricao(self):
        return self.__descricao

    def getDisciplinas(self):
        return self.__disciplinas

    def getProfessores(self):
        return self.__professores

    # ---------- Setters ----------
    def setId(self, id):
        self.__id = id

    def setDescricao(self, descricao):
        self.__descricao = descricao

    # ---------- Curso ↔ Disciplina ----------
    def adicionarDisciplina(self, disciplina):
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)

            if disciplina.getCurso() != self:
                disciplina.setCurso(self)

    def removerDisciplina(self, disciplina):
        if disciplina in self.__disciplinas:
            self.__disciplinas.remove(disciplina)

            if disciplina.getCurso() == self:
                disciplina.setCurso(None)

    # ---------- Curso ↔ Professor ----------
    def adicionarProfessor(self, professor):
        if professor not in self.__professores:
            self.__professores.append(professor)
            professor.adicionarCurso(self)

    def removerProfessor(self, professor):
        if professor in self.__professores:
            self.__professores.remove(professor)
            professor.removerCurso(self)
