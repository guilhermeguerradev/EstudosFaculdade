from .pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, id, nome, cpf, dataNascimento, email, endereco, telefone, identidade,
                 matricula, titulacaoMaxima):
        super().__init__(id, nome, cpf, dataNascimento, email, endereco, telefone, identidade)
        self.__matricula = matricula
        self.__titulacaoMaxima = titulacaoMaxima
        self.__turmas = []    # 0..*
        self.__cursos = []    # N:N

    # ---------- Getters ----------
    def getMatricula(self):
        return self.__matricula

    def getTitulacaoMaxima(self):
        return self.__titulacaoMaxima

    def getTurmas(self):
        return self.__turmas

    def getCursos(self):
        return self.__cursos

    # ---------- Setters ----------
    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setTitulacaoMaxima(self, titulacao):
        self.__titulacaoMaxima = titulacao

    # ---------- Relação Professor ↔ Turma ----------
    def adicionarTurma(self, turma: 'Turma'):
        """Adiciona uma turma ao professor e atualiza o outro lado."""
        if turma not in self.__turmas:
            self.__turmas.append(turma)
            turma.setProfessor(self)

    def removerTurma(self, turma: 'Turma'):
        """Remove a turma do professor e atualiza o outro lado."""
        if turma in self.__turmas:
            self.__turmas.remove(turma)
            turma.setProfessor(None)

    # ---------- Relação Professor ↔ Curso ----------
    def adicionarCurso(self, curso: 'Curso'):
        """Vincula o professor a um curso e atualiza o outro lado."""
        if curso not in self.__cursos:
            self.__cursos.append(curso)
            curso.adicionarProfessor(self)

    def removerCurso(self, curso: 'Curso'):
        """Remove o vínculo entre professor e curso."""
        if curso in self.__cursos:
            self.__cursos.remove(curso)
            curso.removerProfessor(self)