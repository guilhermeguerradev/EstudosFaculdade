class Pessoa:
    def __init__(self, nome, matricula):
        self._nome = nome      
        self._matricula = matricula 

    def get_nome(self):
        return self._nome
    
    def get_matricula(self):
        return self._matricula

    def set_nome(self, novo_nome):
        self._nome = novo_nome
        
    def set_matricula(self, nova_matricula):
        self._matricula = nova_matricula
    
    def mostrar_dados_basicos(self):
        return f"Nome: {self.get_nome()}, Matrícula: {self.get_matricula()}"
