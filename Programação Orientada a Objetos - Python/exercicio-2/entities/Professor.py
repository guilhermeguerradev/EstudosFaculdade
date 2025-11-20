from .Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, matricula, titulacao):
        super().__init__(nome, matricula) 
        self._titulacao = titulacao 

    def get_titulacao(self):
        return self._titulacao

    def set_titulacao(self, nova_titulacao):
        self._titulacao = nova_titulacao

    # Resposta à Q5
    def info_professor(self):
        return f"Professor(a): {self.get_nome()}, Titulação Máxima: {self.get_titulacao()}"