from .Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, matricula, nota1, nota2):
        super().__init__(nome, matricula) 
        self._nota1 = nota1 
        self._nota2 = nota2
    def get_nota1(self):
        return self._nota1
    
    def get_nota2(self):
        return self._nota2

    def set_nota1(self, nova_nota):
        self._nota1 = nova_nota
        
    def set_nota2(self, nova_nota):
        self._nota2 = nova_nota
    
    # Q1: Calcula a média (usa os getters para acessar as notas)
    def calcular_media(self):
        return (self.get_nota1() + self.get_nota2()) / 2
    
    def foi_aprovado(self):
        raise NotImplementedError("Método 'foi_aprovado' deve ser implementado na subclasse.")

    # Q4: Retorna info do aluno e status
    def info_aluno_status(self):
        try:
            status = "Aprovado" if self.foi_aprovado() else "Reprovado"
        except NotImplementedError:
             status = "Regra de Aprovação Indefinida"
             
        return f"Nome: {self.get_nome()}, Matrícula: {self.get_matricula()}, Status: {status}"