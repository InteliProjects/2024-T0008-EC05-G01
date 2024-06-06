function carregarKitsArmazem(nomeKit){
    console.log(nomeKit, "cheguei" )
    var kit = nomeKit

    window.location.href = '/telaKit?kit=' + kit;
}

function voltar(){
    window.location.href = "/telaP";
}