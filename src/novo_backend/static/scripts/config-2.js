function novoKit() {
    var nome;

    while (true) {
        nome = prompt("Digite o nome do kit:");

        if (nome === null) {
            console.log('Operação cancelada pelo usuário.');
            return;
        }

        if (nome.trim() === "") {
            alert("Por favor, preencha todos os campos.");
        } else {
            break;
        }
    }       

    var dados = {
        nome: nome,
        medicamentos: []
    };

    fetch('/kits', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(async response => {
        if (!response.ok) {
            throw new Error('Erro ao criar kit');
        }
        window.location.href = "/kit?kit=" + nome;
    })
    .catch(error => {
        console.error('Erro ao criar kit:', error);
    });
}



function updateKit(kit, dados) {
    var url = window.location.href;
    var url = new URL(url);
    var kit = url.searchParams.get("kit");

    fetch('/kits/'+ kit, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dados),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao adicionar medicamento');
        }
        return response.json();
    })
    .then(data => {
        console.log('Medicamento adicionado com sucesso:', data);
        window.location.href = "/kit?kit=" + kit;
    })
    .catch(error => {
        console.error('Erro ao adicionar medicamento:', error);
    });
}

function atualizarDados() {
    var url = window.location.href;
    var url = new URL(url);
    var kit = url.searchParams.get("kit");

    var medicamentoSelecionado = document.getElementById("medicamentosSelect").value;
    var quantidadeDigitada = document.getElementById("quantidadeInput").value;

    alert("Medicamento selecionado: " + medicamentoSelecionado + "\nQuantidade digitada: " + quantidadeDigitada + "\nKit: " + kit);
    
    var novo_medicamento = {
        nome: medicamentoSelecionado,
        quantidade: quantidadeDigitada,
        altura: 0,
        pos: {
            "x": 0, 
            "y": 0, 
            "z": 0, 
            "r": 0
        }
    };

    fetch('/kits/'+ kit, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao buscar kit');
        }
        return response.json();
    }).then(data => {
        let kit_db = data["kit"]
        kit_db.medicamentos.push(novo_medicamento);
        updateKit(kit, kit_db);
    }).catch(error => {
        console.error('Erro ao buscar kit:', error);
    });
}

function deletarKit(){
    var url = window.location.href;
    var url = new URL(url);
    var kit = url.searchParams.get("kit");

    fetch('/kits/'+ kit, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao deletar kit');
        }
        window.location.href = "/kits";
    }).catch(error => {
        console.error('Erro ao deletar kit:', error);
    });

}

function carregarKits(){
    kit = ""
    console.log("Carregando kits...");

    fetch('/kits/',{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao buscar kit');
        }
        return response.json();
    }).then(data => {
        data.kits.forEach(kit => {
            console.log(kit.nome)});
    }).catch(error => {
        console.error('Erro ao buscar kit:', error);
    });
}
