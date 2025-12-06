
let transactions = [];

// Armazenamos a data de hoje e o mês/ano corrente para referência
const hoje = new Date();
const anoCorrente = hoje.getFullYear();
const mesCorrente = hoje.getMonth() + 1;

// ===========================================
// 2. DOM e Eventos
// ===========================================

const form = document.getElementById('transaction-form');
const transactionsListEl = document.getElementById('transactions-list');
const noDataMsg = document.getElementById('no-data-msg');
const currentBalanceCard = document.getElementById('current-balance');
const balanceValueEl = document.getElementById('current-balance-value');
const balanceStatusEl = document.getElementById('balance-status');
const filtersPanel = document.getElementById('filters-panel');

let currentFilter = 'Todos'; // Estado para o filtro ativo

// Preenche a data de hoje por padrão no input
document.getElementById('data').valueAsDate = hoje;

// -------------------------------------------
// EVENTO 1: SUBMIT do Formulário (Adicionar Transação)
// -------------------------------------------
form.addEventListener('submit', function (event) {
    event.preventDefault();
    handleTransactionSubmit();
});

// -------------------------------------------
// EVENTO 2: CLIQUE nos Botões de Filtro (Mudar o estado do filtro)
// -------------------------------------------
filtersPanel.addEventListener('click', function (event) {
    const filterButton = event.target.closest('.filter-btn');
    if (filterButton) {
        // Atualiza o estado do filtro
        currentFilter = filterButton.dataset.filter;

        // Remove 'active' de todos e adiciona ao clicado
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        filterButton.classList.add('active');

        // Re-renderiza a lista com o novo filtro (Função a ser implementada)
        renderTransactionsList();
    }
});

// -------------------------------------------
// EVENTO 3: DELEÇÃO de Transação (Manipulação de DOM e Array)
// Usamos delegação de eventos para capturar cliques em botões criados dinamicamente
// -------------------------------------------
transactionsListEl.addEventListener('click', function (event) {
    const deleteButton = event.target.closest('.transaction-delete-btn');
    if (deleteButton) {
        // Usa o data-id do elemento (Requisito: dataset)
        const transactionId = parseInt(deleteButton.dataset.id);
        handleDeleteTransaction(transactionId); // Função a ser implementada
    }
});

/**
 * Trata a submissão do formulário de transação, cria o objeto e o armazena.
 */
function handleTransactionSubmit() {
    const dataInput = document.getElementById('data').value;

    // Converte o valor para um número, garantindo o sinal
    const rawValue = parseFloat(document.getElementById('valor').value);
    const tipo = document.getElementById('tipo').value;

    // O valor é negativo se for Despesa, positivo se for Receita
    const valor = tipo === 'Despesa' ? -rawValue : rawValue;

    // Cria o Objeto Transação (Requisito: Objeto)
    const novaTransacao = {
        id: Date.now(), // ID único baseado no timestamp
        valor: valor,
        tipo: tipo,
        data: dataInput,
        categoria: document.getElementById('categoria').value,
        descricao: document.getElementById('descricao').value,
    };

    // Requisito: Array (armazenar itens)
    transactions.push(novaTransacao);

    // Limpa o formulário e reseta a data
    form.reset();
    document.getElementById('data').valueAsDate = hoje;

    // Chama a função principal de atualização (a ser implementada)
    updateAllReports();
}

/**
 * Remove uma transação do Array pelo ID e atualiza o DOM.
 * Implementação básica para evitar erros no commit 12, mas a lógica de remoção será finalizada no commit 14.
 */
function handleDeleteTransaction(id) {
    // Apenas a chamada para a atualização é mantida por enquanto
    // A lógica de filtragem e remoção será completada no próximo commit.
    updateAllReports();
}

/**
 * Função placeholder para renderização e atualização, a ser completada.
 */
function updateAllReports() {
    // Apenas para garantir que o código não quebre neste estágio.
    renderTransactionsList();
}

/**
 * Função placeholder para renderizar a lista, a ser completada.
 */
function renderTransactionsList() {
    // Função a ser implementada no commit 15
    console.log(`Transação adicionada. Total no array: ${transactions.length}`);
}

/**
 * Remove uma transação do Array pelo ID e atualiza o DOM.
 * @param {number} id - O ID único da transação a ser removida.
 */
function handleDeleteTransaction(id) {
    // Requisito: Array (remover item) - Usa filter para criar um novo array sem o item deletado
    transactions = transactions.filter(t => t.id !== id);

    // Atualiza a interface
    updateAllReports();
}

/**
 * Função principal que recalcula e atualiza todos os painéis.
 * Chamada após qualquer alteração nos dados (submit ou delete).
 */
function updateAllReports() {
    // 1. Renderiza a lista de transações (próximo commit)
    renderTransactionsList();

    // 2. Calcula o balanço do mês atual (será implementado no commit 16)
    const balancoMesAtual = calcularBalancoDoMesAtual();

    // 3. Calcula a média mensal para projeção (será implementado no commit 17)
    const mediaMensal = calcularMediaMensalParaProjecao();

    // 4. Atualiza os placares (será implementado nos commits 18 e 19)
    atualizarPlacarDoMesAtual(balancoMesAtual);
    atualizarProjecao(mediaMensal);
}

// -------------------------------------------
// Funções Placeholder de Cálculo (A serem implementadas)
// -------------------------------------------
function calcularBalancoDoMesAtual() {
    return 0; // Placeholder
}
function calcularMediaMensalParaProjecao() {
    return 0; // Placeholder
}
function atualizarPlacarDoMesAtual(balanco) {
    // Placeholder para evitar erro no console
    console.log("Placar atualizado para:", balanco);
}
function atualizarProjecao(mediaMensal) {
    // Placeholder para evitar erro no console
    console.log("Projeção atualizada para:", mediaMensal);
}

/**
 * Renderiza a lista de transações no DOM, aplicando o filtro ativo.
 */
function renderTransactionsList() {
    transactionsListEl.innerHTML = ''; // Limpa a lista antes de re-renderizar

    if (transactions.length === 0) {
        noDataMsg.style.display = 'block';
        return;
    }
    noDataMsg.style.display = 'none';

    // 1. Aplica o filtro (Receita / Despesa / Todos)
    const filteredTransactions = transactions.filter(t => {
        if (currentFilter === 'Todos') return true;
        if (currentFilter === 'Receita') return t.valor > 0;
        if (currentFilter === 'Despesa') return t.valor < 0;
        return true;
    });

    // 2. Ordena por data (mais recente primeiro)
    filteredTransactions.sort((a, b) => new Date(b.data + 'T00:00:00') - new Date(a.data + 'T00:00:00'));

    // 3. Itera e cria elementos (Requisito: Criação dinâmica de elementos)
    filteredTransactions.forEach(t => {
        const listItem = document.createElement('li');
        listItem.classList.add('transaction-item');

        const valorFormatado = Math.abs(t.valor).toFixed(2).replace('.', ',');
        const sinal = t.valor > 0 ? '+' : '-';
        const valorClasse = t.valor > 0 ? 'positive' : 'negative';

        listItem.innerHTML = `
            <div class="transaction-details">
                <strong>${t.data} - ${t.categoria}</strong> 
                <p>${t.descricao || 'Sem descrição'}</p>
            </div>
            <span class="transaction-value ${valorClasse}">${sinal} R$ ${valorFormatado}</span>
            <button class="transaction-delete-btn" data-id="${t.id}">✖</button>
        `;

        transactionsListEl.appendChild(listItem);
    });
}

// *******************************************
// 4. Lógica de Cálculo Mensal e Projeção (Início da Implementação)
// *******************************************

/**
 * Filtra e calcula o balanço total apenas para o mês e ano corrente.
 * @returns {number} O balanço total do mês atual.
 */
function calcularBalancoDoMesAtual() {
    const transacoesDoMes = transactions.filter(t => {
        // Adiciona 'T00:00:00' para evitar problemas de fuso horário na comparação
        const dataTransacao = new Date(t.data + 'T00:00:00');

        // Compara Ano e Mês (getMonth() é base 0, por isso usamos mesCorrente que é base 1)
        return dataTransacao.getFullYear() === anoCorrente &&
            (dataTransacao.getMonth() + 1) === mesCorrente;
    });

    // Requisito: Array (usar reduce para somar o balanço)
    return transacoesDoMes.reduce((acc, curr) => acc + curr.valor, 0);
}

/**
 * Função placeholder para cálculo de média mensal (será implementada no commit 17).
 */
function calcularMediaMensalParaProjecao() {
    return 0;
}

/**
 * Calcula a média de balanço mensal com base nos dados históricos.
 * Usamos os últimos 3 meses registrados como referência para uma projeção mais estável.
 * @returns {number} A média mensal dos últimos 3 meses.
 */
function calcularMediaMensalParaProjecao() {
    if (transactions.length === 0) return 0;

    // 1. Agrupa o balanço (Receitas - Despesas) por ano-mês (YYYY-MM)
    const balancoPorMes = transactions.reduce((acc, t) => {
        // Usa 'T00:00:00' para evitar problemas de fuso horário
        const data = new Date(t.data + 'T00:00:00');
        // Cria chave YYYY-MM
        const anoMes = data.getFullYear() + '-' + (data.getMonth() + 1).toString().padStart(2, '0');

        if (!acc[anoMes]) {
            acc[anoMes] = 0;
        }
        acc[anoMes] += t.valor;
        return acc;
    }, {});

    // 2. Ordena os meses (mais recente primeiro)
    const mesesOrdenados = Object.keys(balancoPorMes).sort().reverse();

    // 3. Pega os últimos 3 meses para cálculo da média
    // (O número de meses pode ser menor que 3 se não houver dados suficientes)
    const ultimos3Meses = mesesOrdenados.slice(0, 3);

    if (ultimos3Meses.length === 0) return 0;

    // 4. Soma o balanço desses 3 meses
    const somaDosUltimosMeses = ultimos3Meses.reduce((soma, mes) => soma + balancoPorMes[mes], 0);

    // 5. Calcula a média e retorna
    return somaDosUltimosMeses / ultimos3Meses.length;
}

// *******************************************
// 5. Atualização dos Painéis (Início da Implementação)
// *******************************************

/**
 * Atualiza o placar principal com o Balanço do Mês Atual.
 * @param {number} balanco - O valor total do balanço do mês corrente.
 */
function atualizarPlacarDoMesAtual(balanco) {
    // 1. Define a classe e o texto de status com base no balanço
    const valorClasse = balanco > 0 ? 'positive' : balanco < 0 ? 'negative' : 'neutral';
    const statusTexto = balanco > 0 ? 'Meta Positiva! 💪' : balanco < 0 ? 'Atenção: Mês Negativo 🚩' : 'Balanço Zerado até agora';

    // 2. Formata o balanço para exibição
    const balancoFormatado = balanco.toFixed(2).replace('.', ',');
    balanceValueEl.textContent = `R$ ${balancoFormatado}`;
    balanceStatusEl.textContent = statusTexto;

    // 3. Remove classes anteriores (Limpeza)
    const classes = ['positive', 'negative', 'neutral', 'status-positive', 'status-negative', 'status-neutral'];
    balanceValueEl.classList.remove(...classes);
    balanceStatusEl.classList.remove(...classes);
    currentBalanceCard.classList.remove(...classes);

    // 4. Adiciona novas classes (Requisito: classList.add)
    balanceValueEl.classList.add(valorClasse);
    balanceStatusEl.classList.add(`status-${valorClasse}`);
    currentBalanceCard.classList.add(`status-${valorClasse}`);

    // 5. Atualiza o título para exibir o mês/ano corrente
    currentBalanceCard.querySelector('h3').textContent = `Balanço do Mês Atual (${mesCorrente}/${anoCorrente})`;
}

/**
 * Função placeholder para projeção (será implementada no commit 19).
 */
function atualizarProjecao(mediaMensal) {
    // Placeholder para evitar erro no console
    console.log("Projeção será atualizada em breve.");
}

/**
 * Atualiza o painel de projeção para o Próximo Mês.
 * @param {number} mediaMensal - A média de balanço mensal calculada.
 */
function atualizarProjecao(mediaMensal) {
    const mediaFormatada = mediaMensal.toFixed(2).replace('.', ',');

    // A projeção para o Próximo Mês é simplesmente a Média Mensal calculada

    document.getElementById('daily-avg-value').textContent = `R$ ${mediaFormatada}`;
    document.getElementById('weekly-projection-value').textContent = `R$ ${mediaFormatada}`;

    // Confirma que os textos dos labels estão corretos para a análise mensal
    document.getElementById('daily-avg-value').parentElement.querySelector('span').previousSibling.textContent = 'Média Mensal: ';
    document.getElementById('weekly-projection-value').parentElement.querySelector('span').previousSibling.textContent = 'Projeção Próx. Mês: ';
}

// ===========================================
// 6. Inicialização
// ===========================================

/**
 * Função principal que recalcula e atualiza todos os painéis.
 * (Função finalizada no commit 14, garantindo que todas as sub-funções sejam chamadas).
 */
function updateAllReports() {
    renderTransactionsList();

    // 2. Calcula o balanço do mês atual (Implementado no commit 16)
    const balancoMesAtual = calcularBalancoDoMesAtual();

    // 3. Calcula a média mensal para projeção (Implementado no commit 17)
    const mediaMensal = calcularMediaMensalParaProjecao();

    // 4. Atualiza os placares (Implementado nos commits 18 e 19)
    atualizarPlacarDoMesAtual(balancoMesAtual);
    atualizarProjecao(mediaMensal);
}

// Inicialização: carrega os relatórios
document.addEventListener('DOMContentLoaded', updateAllReports);