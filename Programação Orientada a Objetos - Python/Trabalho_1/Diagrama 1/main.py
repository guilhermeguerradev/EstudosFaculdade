from entities.empresa import Empresa
from entities.participante import Participante
from entities.produto import Produto
from entities.itemNota import ItemNota
from entities.nota import Nota


def main():
    empresa = Empresa(1, 101, "Tech Solutions", "Rua das Flores, 100", "12.345.678/0001-99")
    participante = Participante(1, 202, "Cliente XPTO", "987.654.321-00")

    produto1 = Produto(1, "P001", "Mouse Gamer RGB")
    produto2 = Produto(2, "P002", "Teclado Mecânico RGB")
    produto3 = Produto(3, "P003", "Monitor 27'' Full HD")

    item1 = ItemNota(1, 150.00, 2, None, produto1)
    item2 = ItemNota(2, 350.00, 1, None, produto2)
    item3 = ItemNota(3, 900.00, 1, None, produto3)

    nota = Nota(1, "2025-10-14", 1001, item1, empresa, participante)

    nota.addItemNota(item2)
    nota.addItemNota(item3)

    item1.setNota(nota)
    item2.setNota(nota)
    item3.setNota(nota)

    # --- Exibindo resultados ---
    print("=== NOTA ===")
    print(f"ID: {nota.getId()}")
    print(f"Número: {nota.getNumero()}")
    print(f"Data: {nota.getData()}")
    print(f"Empresa: {nota.getEmpresa().getRazaoSocial()}")
    print(f"Participante: {nota.getParticipante().getRazaoSocial()}")

    print("\n=== ITENS ===")
    for it in nota.getItensNota():
        print(f"- Produto: {it.getProduto().getDescricao()}")
        print(f"  Valor unitário: {it.getVrUnitario()}")
        print(f"  Quantidade: {it.getQuantidade()}")
        print(f"  Total do item: {it.getTotal()}")

    print(f"\nValor total da nota: {nota.getVrTotal()}")


if __name__ == "__main__":
    main()
