function exibirResultado(opcoes, nomeCliente, cnpjCliente) {
    const resultadoDiv = document.getElementById('resultadoDiv');
    resultadoDiv.innerHTML = `
        <h2>Opções de sistema ideal para o cliente:</h2>
        <p>Cliente: ${nomeCliente}</p>
        <p>CNPJ: ${cnpjCliente}</p>
        <ul class="resultado">
            ${opcoes.map(opcao => `<li>${opcao} <a href="#" id="btnLink">Gerar</a></li>`).join('')}
        </ul>
        <h5>Ao clicar em gerar, será incluido na página de orçamento!</h5>`;
        
    
    resultadoDiv.style.display = 'block';
}