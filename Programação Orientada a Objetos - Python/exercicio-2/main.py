
from entities import Pessoa, Professor, AlunoEnsinoMedio, AlunoGraduacao

# ---------------------------------------------
# DADOS DE TESTE
# ---------------------------------------------

# Alunos de Ensino Médio (Regra de Aprovação: Média >= 6.0)
# Aprovado: (5.5 + 6.5) / 2 = 6.0
aluno_em_aprovado = AlunoEnsinoMedio("Ana Souza", "EM101", 5.5, 6.5) 
# Reprovado: (4.0 + 5.0) / 2 = 4.5
aluno_em_reprovado = AlunoEnsinoMedio("Bruno Lima", "EM102", 4.0, 5.0)

# Alunos de Graduação (Regra de Aprovação: Média >= 7.0)
# Aprovado: (7.0 + 8.0) / 2 = 7.5
aluno_gr_aprovado = AlunoGraduacao("Carla Diniz", "GR201", 7.0, 8.0) 
# Reprovado: (6.0 + 7.5) / 2 = 6.75
aluno_gr_reprovado = AlunoGraduacao("David Mendes", "GR202", 6.0, 7.5)

# Professor
professor = Professor("Dra. Elza Vieira", "PR005", "Doutorado")

# ---------------------------------------------
# TESTES E RESPOSTAS ÀS QUESTÕES
# ---------------------------------------------

if __name__ == "__main__":
    print("==============================================")
    print("           RELATÓRIO DE APROVAÇÃO (OO)")
    print("==============================================\n")
    
    

    print("--- 📝 Teste de Alunos (Polimorfismo para Q2 e Q3) ---")
    
    lista_alunos = [aluno_em_aprovado, aluno_em_reprovado, aluno_gr_aprovado, aluno_gr_reprovado]
    
    for aluno in lista_alunos:
        # Q1: Calcular a média das duas notas
        media = aluno.calcular_media()
        
        # Q2 & Q3: Verificar aprovação (Lógica diferente dependendo da classe)
        aprovado = "SIM" if aluno.foi_aprovado() else "NÃO"
        
        # Q4: Retornar Nome, Matrícula e Status
        tipo_aluno = "Ensino Médio" if isinstance(aluno, AlunoEnsinoMedio) else "Graduação"
        
        print(f"\n[ {tipo_aluno} ]")
        print(f"  {aluno.get_nome()} ({aluno.get_matricula()})")
        print(f"  Média (Q1): {media:.2f}")
        print(f"  Aprovado (Q2/Q3): {aprovado}")
        print(f"  Relatório Completo (Q4): {aluno.info_aluno_status()}")


    ## Resposta Q5

    print("\n--- 🧑‍🏫 Teste de Professor (Q5) ---")
    
    # Q5: Retornar o nome do professor e sua titulação máxima
    print(f"Relatório Professor (Q5): {professor.info_professor()}")

    

    print("\n--- 🔒 Teste de Encapsulamento (Getter/Setter) ---")

    # 1. Antes de usar o Setter:
    print(f"Nome Inicial de Bruno: {aluno_em_reprovado.get_nome()}")
    print(f"Nota 1 Inicial de Bruno: {aluno_em_reprovado.get_nota1()}")
    print(f"Status Inicial de Bruno: {aluno_em_reprovado.info_aluno_status()}") 

    # 2. Usando Setter para correção:
    print("-> Correção da Nota 1 (Setter)...")
    aluno_em_reprovado.set_nota1(7.0) # Muda a nota de 4.0 para 7.0

    # 3. Após usar o Setter (Média: (7.0 + 5.0) / 2 = 6.0 -> Aprovado)
    print(f"Nota 1 Após Correção: {aluno_em_reprovado.get_nota1()}")
    print(f"Status Final de Bruno: {aluno_em_reprovado.info_aluno_status()}")
    
    print("\n==============================================")