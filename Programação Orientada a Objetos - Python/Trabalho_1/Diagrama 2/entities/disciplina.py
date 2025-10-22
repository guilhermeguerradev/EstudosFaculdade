class Disciplina:
    def __init__(self, id, descricao, curso):
        self.__id = id
        self.__descricao = descricao
        self.__curso = curso
        self.__turmas = []  # 0..*

        # Quando cria a disciplina, ela já é adicionada ao curso
        curso.adicionarDisciplina(self)

    # ---------- Getters ----------
    def getId(self):
        return self.__id

    def getDescricao(self):
        return self.__descricao

    def getCurso(self):
        return self.__curso

    def getTurmas(self):
        return self.__turmas

    # ---------- Setters ----------
    def setId(self, id):
        self.__id = id

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setCurso(self, curso):
        self.__curso = curso

    # ---------- Disciplina ↔ Turma ----------
    def adicionarTurma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)
            turma.setDisciplina(self)

    def removerTurma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            turma.setDisciplina(None)
