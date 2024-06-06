function adicionar() {
    var fila = [];
    while (true) {
        var nome = prompt("Digite o nome do kit que deseja executar ou clique em 'Cancelar' para parar: ");
        if (nome === null) {
            break;
        }
        fila.push(nome);
    }

    console.log(fila);

    var index = 0;

    function enviarProximoKit() {
        if (index < fila.length) { 
            var kitAtual = fila[index];
            fetch(`/fila/${kitAtual}`, { 
                method: 'GET', 
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(async response => {
                if (!response.ok) {
                    throw new Error('Erro ao adicionar kit na fila');
                }
                if (response.ok) {
                    alert("Kit adicionado com sucesso!");
                    console.log('Kit adicionado com sucesso:', kitAtual);
                    index++; 
                    enviarProximoKit(); 
                }
            })
            .catch(error => {
                console.error('Erro ao adicionar kit na fila:', error);
            });
        } else {
            window.location.href = "/auxiliar";
        }
    }
    enviarProximoKit();
}
