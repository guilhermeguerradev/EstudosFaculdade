from .Aluno import Aluno


class AlunoEnsinoMedio(Aluno):
    # Q2: Regra: média deve ser maior ou igual a 6
    def foi_aprovado(self):
        return self.calcular_media() >= 6.0