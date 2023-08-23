function gerarOrcamento() {
    const form = document.querySelector('form')
    const formData = new FormData(form)

    fetch('/home/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        exibirResultado(data.opcoes_orcamento, data.nome_cliente, data.cnpj)
    })
    .catch(error => {
        console.error('Erro:', error)
    })
}