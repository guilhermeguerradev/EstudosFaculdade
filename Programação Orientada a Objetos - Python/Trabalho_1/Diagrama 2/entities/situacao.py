from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .aluno import Aluno


class Situacao:
    def __init__(self, situacao, anoSemestre, aluno=None):
        self.__situacao = situacao
        self.__anoSemestre = anoSemestre
        self.__alunos = []

        if aluno:
            self.adicionarAluno(aluno)

    # ---------- Getters ----------
    def getSituacao(self):
        return self.__situacao

    def getAnoSemestre(self):
        return self.__anoSemestre

    def getAlunos(self):
        return self.__alunos

    # ---------- Setters ----------
    def setSituacao(self, situacao):
        self.__situacao = situacao

    def setAnoSemestre(self, anoSemestre):
        self.__anoSemestre = anoSemestre

    # ---------- Métodos de Associação ----------
    def adicionarAluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)
            aluno.adicionarSituacao(self)

    def removerAluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            aluno.removerSituacao(self)