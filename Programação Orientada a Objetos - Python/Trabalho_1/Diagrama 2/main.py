from datetime import date
from decimal import Decimal

# ---------- IMPORTS ----------
from entities.aluno import Aluno
from entities.professor import Professor
from entities.instituicao import Instituicao
from entities.disciplina import Disciplina
from entities.curso import Curso
from entities.turma import Turma
from entities.diario import Diario
from entities.situacao import Situacao


def main():
    print("===== TESTE COMPLETO DO SISTEMA ACADÊMICO =====\n")

    # ---------- INSTITUIÇÃO ----------
    inst1 = Instituicao(1, "UniAcademia")
    print(f"Instituição criada: {inst1.getDescricao()}")

    # ---------- CURSOS ----------
    curso1 = Curso(10, "Engenharia de Software")
    curso2 = Curso(11, "Direito")
    curso3 = Curso(12, "Odontologia")

    print("\nCursos cadastrados:")
    for c in [curso1, curso2, curso3]:
        print(f"- {c.getDescricao()}")

    # ---------- PROFESSORES ----------
    prof1 = Professor(100, "Maria Paula", "111.222.333-44", date(1980, 1, 20),
                      "maria@uni.com", "Av. Brasil", "98888-1111", "MG-121212",
                      "P001", 3)

    prof2 = Professor(101, "João Pedro", "555.666.777-88", date(1975, 6, 18),
                      "joao@uni.com", "Av. JK", "98888-2222", "MG-343434",
                      "P002", 2)

    prof3 = Professor(102, "Luciana Alves", "999.000.111-22", date(1990, 9, 12),
                      "luciana@uni.com", "Rua Centro", "98888-3333", "MG-565656",
                      "P003", 4)

    print("\nProfessores cadastrados:")
    for p in [prof1, prof2, prof3]:
        print(f"- {p.getNome()} (Titulação: {p.getTitulacaoMaxima()})")

    # ---------- SITUAÇÕES ----------
    sit1 = Situacao("Ativo", 20231)
    sit2 = Situacao("Trancado", 20232)
    sit3 = Situacao("Concluído", 20241)

    # ---------- ALUNOS ----------
    aluno1 = Aluno(200, "Guilherme Guerra", "123.123.123-12", date(2001, 7, 15),
                   "guerra@email.com", "Rua Verde", "99999-0000", "MG-998877",
                   "A001", 2023, 1, sit1)

    aluno2 = Aluno(201, "Beatriz Rocha", "321.321.321-32", date(2002, 3, 22),
                   "bia@email.com", "Rua Amarela", "99999-1111", "MG-776655",
                   "A002", 2023, 1, sit2)

    aluno3 = Aluno(202, "Caio Souza", "111.333.555-77", date(2000, 9, 8),
                   "caio@email.com", "Rua Azul", "99999-2222", "MG-445566",
                   "A003", 2024, 1, sit3)

    print("\nAlunos criados:")
    for a in [aluno1, aluno2, aluno3]:
        print(f"- {a.getNome()} ({a.getSituacoes()[0].getSituacao()})")

    # ---------- DISCIPLINAS ----------
    disc1 = Disciplina(300, "POO", curso1)
    disc2 = Disciplina(301, "Estrutura de Dados", curso1)
    disc3 = Disciplina(302, "Banco de Dados", curso1)

    print("\nDisciplinas adicionadas ao curso Engenharia de Software:")
    for d in curso1.getDisciplinas():
        print(f"- {d.getDescricao()}")

    # ---------- TURMAS ----------
    turma1 = Turma(400, "Turma A", 2025, 1, prof1, inst1, disc1)
    turma2 = Turma(401, "Turma B", 2025, 1, prof2, inst1, disc2)
    turma3 = Turma(402, "Turma C", 2025, 2, prof3, inst1, disc3)

    print("\nTurmas criadas:")
    for t in inst1.getTurmas():
        print(f"- {t.getDescricao()} ({t.getDisciplina().getDescricao()}) - Prof: {t.getProfessor().getNome()}")

    # ---------- DIÁRIOS ----------
    d1 = Diario(Decimal("8.5"), Decimal("7.0"), Decimal("9.0"), Decimal("8.2"), 2, aluno1, turma1)
    d2 = Diario(Decimal("6.0"), Decimal("7.5"), Decimal("8.0"), Decimal("7.2"), 1, aluno2, turma1)
    d3 = Diario(Decimal("9.0"), Decimal("8.5"), Decimal("9.5"), Decimal("9.0"), 0, aluno3, turma2)

    print("\nNotas registradas:")
    for d in [d1, d2, d3]:
        print(f"- {d.getAluno().getNome()} na {d.getTurma().getDescricao()}: VT = {d.getVT()} | Faltas = {d.getFaltas()}")

    # ---------- TESTE DE RELAÇÕES ----------
    print("\n===== RELAÇÕES BIDIRECIONAIS =====")
    print(f"{prof1.getNome()} leciona {len(prof1.getTurmas())} turma(s).")
    print(f"A instituição {inst1.getDescricao()} possui {len(inst1.getTurmas())} turma(s).")
    print(f"O curso {curso1.getDescricao()} tem {len(curso1.getDisciplinas())} disciplina(s).")
    print(f"O aluno {aluno1.getNome()} tem {len(aluno1.getSituacoes())} situação(ões) registradas.")

    print("\n===== TESTE FINAL =====")
    print(f"Turma {turma1.getDescricao()} → Professor: {turma1.getProfessor().getNome()} | "
          f"Disciplina: {turma1.getDisciplina().getDescricao()} | "
          f"Instituição: {turma1.getInstituicao().getDescricao()}")


if __name__ == "__main__":
    main()
