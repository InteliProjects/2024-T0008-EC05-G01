function passarUrlReabastecimento(){
    var url = window.location.href;
    var url = new URL(url);
    var item = url.searchParams.get("item");

    window.location.href = "/configReabastecimento?item=" + item;
}

console.log("hello world");
// Função para carregar dinamicamente as opções de medicamentos
function carregarMedicamentos() {
    fetch('/medicamentos')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('medicamentosSelect');

            select.innerHTML = '';
    
            const placeholderOption = document.createElement('option');
            placeholderOption.value = '';
            placeholderOption.text = 'Selecione um medicamento';
            placeholderOption.disabled = true;
            placeholderOption.selected = true;
            select.appendChild(placeholderOption);
    
            for (const key in data.medicamentos) {
                if (data.medicamentos.hasOwnProperty(key)) {
                    const medicamento = data.medicamentos[key];
                    const option = document.createElement('option');
                    option.value = medicamento.nome;
                    option.text = medicamento.nome;
                    select.appendChild(option);
                }
            }

        })
        .catch(error => console.error('Erro ao carregar medicamentos:', error));
}
carregarMedicamentos();