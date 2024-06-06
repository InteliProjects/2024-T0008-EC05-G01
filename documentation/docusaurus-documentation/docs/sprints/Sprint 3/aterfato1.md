---
title: Artefato - Hardware Periférico
sidebar_position: 1
---

# Por que escolhemos utilizar um periférico em nossa solução:

&emsp;Os periféricos desempenham um papel crucial em nossa solução de IoT. Embora não sejam elementos essenciais para o funcionamento do sistema, eles contribuem significativamente para aumentar a qualidade e a eficiência das tarefas executadas. Ao integrar periféricos em nossa solução, elevamos a assertividade e garantimos um serviço de maior qualidade.

## Qual periférico escolhemos e por que:

&emsp;Optamos por integrar o sensor seguidor de linha TCRT5000, conhecido como sensor infravermelho, em nossa solução. Este periférico desempenha um papel fundamental ao garantir que o braço robótico execute suas tarefas com precisão. Ele atua como um mecanismo de verificação para a garra/ventosa acoplada à ponta do braço robótico. Se o sensor detectar a presença de material coletado, o processo continua normalmente. No entanto, caso não haja material identificado, o robô emite um aviso sonoro e executa a última tarefa atribuída a ele. Essa abordagem garante que os medicamentos sejam adequadamente coletados pela garra, minimizando possíveis divergências durante a montagem do kit médico.

## Demonstração visual do sensor TCRT5000:

<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 01 - Sensor TCRT5000</p>
    ![image](/img/sensor-TCRT5000.jpg)
    <p>Fonte: disponível em <a href="https://www.google.com/url?sa=i&url=https%3A%2F%2Fmultilogica-shop.com%2Fprodutos%2Fsensor-optico-reflexivo-tcrt5000%2F&psig=AOvVaw0ij8kY8Xv2yhGNaDbbbAjY&ust=1710353065062000&source=images&cd=vfe&opi=89978449&ved=0CBUQjhxqFwoTCMCj0tOq74QDFQAAAAAdAAAAABAE" target="_blank">clique aqui</a></p>
</div>

## Quais componentes compõem nosso circuito junto ao periférico:

&emsp;Para a construção do nosso circuito e utilização do periférico, estamos utilizando os seguintes componentes descritos na tabela abaixo:

<div style={{width: '40%', margin: '0 auto', textAlign: 'center'}}>
    <p>Tabela 01 - Listagem dos componentes</p>
    <table>
        <thead>
            <tr>
                <th>Componente</th>
                <th>Quantidade</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>LED vermelho</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Sensor seguidor de linha TCRT5000</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Resistor de 330 Ω</td>
                <td>3 unidades</td>
            </tr>
            <tr>
                <td>Buzzer</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Jumper macho-macho</td>
                <td>11 unidades</td>
            </tr>
            <tr>
                <td>Placa Raspberry Pi Pico</td>
                <td>1 unidade</td>
            </tr>
            <tr>
                <td>Protoboard</td>
                <td>1 unidade</td>
            </tr>
        </tbody>
    </table>
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;A partir desses componentes, é possível montar nosso circuito para a utilização do periférico TCRT5000.

## Guia de montagem:

&emsp;Placa que estamos utilizando para a construção do nosso circuito e seus respectivos pinos:

<div style={{width: '75%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 02 - Representação das portas da placa</p>
    ![image](/img/picow-pinout.svg)
    <p>Fonte: disponível em <a href="https://murilo-zc.github.io/M5-Inteli-Eng-Comp/Material/Semana-05/instrucao53/#41-apresenta%C3%A7%C3%A3o-da-forma-de-programar-o-raspberry-pi-pico-em-python" target="_blank">clique aqui</a></p>
</div>

&emsp;Representação do nosso circuito final para o periférico feito no software kicad:

<div style={{width: '75%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 03 - Representação do software kicad</p>
    ![image](/img/kicad-circuito.png)
    <p>Fonte: Elaboração própia</p>
</div>

&emsp;Realize a conexão entre o GND e a saída de 3V3 da placa na protoboard para poder energizar o circuito, estamos usando o pino 5 para a saída de energia e o pino 23 para o GND:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 04 - Conexão das saídas da placa a protoboard</p>
    ![image](/img/conexao-positivo-negativo-placa.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Agora, iremos ligar a o outro lado da placa, da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 05 - Conexão da protoboard inteira</p>
    ![image](/img/conexao-positivo-negativo.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;1. Agora que a protoboard está energizada corretamente, o primeiro passo para começar a construir nosso circuito é encaixar a placa Raspberry Pi Pico na protoboard com cuidado como mostra a imagem abaixo:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 06 - Montagem da Raspberry Pi Pico na protoboard</p>
    ![image](/img/placa-protoboard.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;2. Agora iremos realizar a montagem do nosso LED vermelho ao circuito. Será necessário nesta etapa:

   - 1 Resistor de 330 Ω
   - 2 Jumpers macho-macho

&emsp;Para melhor entendimento de como posicionar o LED em nossa protoboard, vamos visualizar como funcionam os terminais de um LED observando a seguinte imagem:

<div style={{width: '70%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 07 - Exemplo de um LED e seus terminais</p>
    ![image](/img/led-exemplo.png)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Realize o posicionamento do LED na protoboard da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 08 - Posicionamento do LED na protoboard</p>
    ![image](/img/led-placa-protoboard.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Conecte um dos terminais do resistor no terminal negativo do LED:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 09 - Conexão entre o terminal negativo do LED e o resistor</p>
    ![image](/img/led-resistor.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Conecte o terminal negativo (cátodo) do LED ao GND (terra) da protoboard para fechar o circuito corretamente.

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 10 - Conexão entre o terminal negativo do LED e o GND da protoboard</p>
    ![image](/img/led-gnd.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Conecte o terminal positivo (ânodo) do LED a uma porta lógica específica da placa (por exemplo, GPIO pin 17), conforme indicado no seu código. Certifique-se de seguir as instruções de pinagem corretamente para evitar erros de conexão.

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 11 - Conexão do terminal positivo do LED a uma porta lógica da placa</p>
    ![image](/img/conexão-pl-final-led.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Aqui estamos conectando o terminal positivo do LED a porta lógica da placa número xx:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 12 - Conexão do terminal positivo do LED a uma porta lógica da placa parte 2</p>
    ![image](/img/conexão-pl-led.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;3. Agora iremos montar o nosso sensor TCRT5000, primeiro passo é conectá-lo na protoboard desta forma:

&emsp;Realize o posicionamento do sensor na protoboard da seguinte maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 13 - Posicionamento do sensor na protoboard</p>
    ![image](/img/posicionamento-infra.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Primeiro, iremos conectar um dos lados do sensor ao resistor dessa maneira:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 14 - Posicionamento do resistor na protoboard</p>
    ![image](/img/resistor-infra.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Agora precisamos conectar o ground (GND) a um terminal do nosso sensor:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 15 - Posicionamento do GND do sensor na protoboard</p>
    ![image](/img/conexao-infra-gnd.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Iremos replicar esses últimos dois passos para o outro lado do sensor:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 16 - Posicionamento do resistor na protoboard</p>
    ![image](/img/resistor-infra.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 17 - Posicionamento do GND do sensor na protoboard</p>
    ![image](/img/conexao-infra-gnd.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Para conectar o buzzer, é necessário conectar o positivo ao pino de 3V3 e o negativo ao GND:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 18 - Conecxão do buzzer</p>
    ![image](/img/buzzer.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;Por último, iremos conectar o sensor à nossa porta lógica GP26_AQ(porta 31) na placa, da seguinte forma:

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 19 - Posicionamento do sensor em uma porta lógica na placa</p>
    ![image](/img/conexao-pl-infra.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 20 - Posicionamento final do sensor na protoboard</p>
    ![image](/img/conexa-final-infra.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

## Circuito ao terminar sua montagem:

&emsp;E por fim, nosso circuito deve estar parecido com algo assim no final de sua montagem (a placa está separada, entretanto as conexões que levam até ela estão posicionadas da mesma maneira descrita):

<div style={{width: '50%', margin: '0 auto', textAlign: 'center'}}>
    <p>Imagem 21 - Montagem final do circuito</p>
    ![image](/img/circuito-final.jpeg)
    <p>Fonte: Elaboração própria</p>
</div>

&emsp;A compreensão da montagem do circuito deve ficar clara ao encarregado de seguir o passo a passo. Caso seja necessário um melhor entendimento do circuito, entre em contato com a seguinte organização que representa o grupo ARM <a href="https://www.linkedin.com/school/inteli-edu/mycompany/" target="_blank">clicando aqui</a>.
