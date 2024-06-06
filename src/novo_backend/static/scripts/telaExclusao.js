function deletarKit(nomeKit) {
    var kit = nomeKit

    fetch('/kits/' + kit, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        }
    }).then(response => {
        if (!response.ok) {
            throw new Error('Erro ao excluir kit');
        }
        return response.json();
    }).then(data => {
        console.log('Kit excluído com sucesso:', data);
        alert('Kit excluído com sucesso!');
        window.location.href = "/telaP";
    }).catch(error => {
        console.error('Erro ao excluir kit:', error);
    });
}

function passarKit(){
    var url = window.location.href;
    var url = new URL(url);
    var kit = document.getElementById('nome').textContent;
    window.location.href = "/deleteKit?kit=" + kit;
}