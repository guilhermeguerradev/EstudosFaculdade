from .Aluno import Aluno


class AlunoGraduacao(Aluno):
    # Q3: Regra: média deve ser maior ou igual a 7
    def foi_aprovado(self):
        return self.calcular_media() >= 7.0