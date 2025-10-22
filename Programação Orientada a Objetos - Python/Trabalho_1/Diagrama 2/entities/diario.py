class Diario:
    def __init__(self, v1, v2, v3, vT, faltas, aluno, turma):
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__vT = vT     # corrigido: antes estava "vt" minúsculo
        self.__faltas = faltas
        self.__aluno = aluno
        self.__turma = turma

        # Cria os vínculos nos dois lados
        aluno.adicionarDiario(self)
        turma.adicionarDiario(self)

    # ---------- Getters ----------
    def getV1(self):
        return self.__v1

    def getV2(self):
        return self.__v2

    def getV3(self):
        return self.__v3

    def getVT(self):
        return self.__vT

    def getFaltas(self):
        return self.__faltas

    def getAluno(self):
        return self.__aluno

    def getTurma(self):
        return self.__turma

    # ---------- Setters ----------
    def setV1(self, v1):
        self.__v1 = v1

    def setV2(self, v2):
        self.__v2 = v2

    def setV3(self, v3):
        self.__v3 = v3

    def setVT(self, vT):
        self.__vT = vT

    def setFaltas(self, faltas):
        self.__faltas = faltas

    def setAluno(self, aluno):
        self.__aluno = aluno
        aluno.adicionarDiario(self)

    def setTurma(self, turma):
        self.__turma = turma
        turma.adicionarDiario(self)
