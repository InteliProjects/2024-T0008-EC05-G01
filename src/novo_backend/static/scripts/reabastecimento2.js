function novoItem() {
    var nome;

    while (true) {
        nome = prompt("Digite o nome do item: ");
        quantidade = prompt("Digite a quantidade do item: ")

        if (nome === null || quantidade === null) {
            console.log('Operação cancelada pelo usuário.');
            return;
        }

        if (nome.trim() === "" && quantidade.trim() === "") {
            alert("Por favor, preencha todos os campos.");
        } else {
            break;
        }
    }       

    var dados = {
        nome: nome,
        quantidade: quantidade
    };

    fetch('/item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(async response => {
        if (!response.ok) {
            throw new Error('Erro ao inserir item no estoque');
        }
        if (response.ok){
            alert("Item: " + nome + "\nQuantidade digitada: " + quantidade);
            window.location.href = "/reabastecimento"
        }
        // window.location.href = "/item?item=" + nome;
    })
    .catch(error => {
        console.error('Erro ao criar item:', error);
    });
}